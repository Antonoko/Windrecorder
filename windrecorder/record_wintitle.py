# 记录活动前台的窗口标题名
import datetime
import os
import re

import pandas as pd
import pygetwindow
import streamlit as st

from windrecorder import file_utils, utils
from windrecorder.config import config
from windrecorder.oneday import OneDay
from windrecorder.utils import get_text as _t

CSV_TEMPLATE_DF = pd.DataFrame(columns=["datetime", "window_title"])
window_title_last_record = ""


def get_csv_filepath(datetime: datetime.datetime):
    """取得对应 datetime 的 wintitle csv 路径"""
    csv_filename = datetime.strftime("%Y-%m-%d") + ".csv"
    csv_filepath = os.path.join(config.win_title_dir, csv_filename)
    return csv_filepath


def record_wintitle_now():
    """记录当下的前台窗口标题到 csv"""
    global window_title_last_record
    windowTitle = optimize_wintitle_name(str(pygetwindow.getActiveWindowTitle()))

    # 如果与上次检测结果一致，则跳过
    if windowTitle == window_title_last_record:
        return

    csv_filepath = get_csv_filepath(datetime.datetime.now())
    if not os.path.exists(csv_filepath):
        file_utils.ensure_dir(config.win_title_dir)
        file_utils.save_dataframe_to_path(CSV_TEMPLATE_DF, file_path=csv_filepath)

    df = file_utils.read_dataframe_from_path(file_path=csv_filepath)

    new_data = {
        "datetime": datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"),
        "window_title": windowTitle,
    }
    df.loc[len(df)] = new_data
    file_utils.save_dataframe_to_path(df, file_path=csv_filepath)
    window_title_last_record = windowTitle  # 更新本轮检测结果


def get_wintitle_by_timestamp(timestamp: int):
    """根据输入时间戳，搜寻对应窗口名。"""
    # 规则：如果离后边记录的时间超过1s，则取上一个的记录
    target_time = utils.seconds_to_datetime(timestamp)
    csv_filepath = get_csv_filepath(target_time)
    if not os.path.exists(csv_filepath):
        return None

    df = file_utils.read_dataframe_from_path(file_path=csv_filepath)
    df["datetime"] = pd.to_datetime(df["datetime"])

    # 从dataframe中查找时间戳对应的window_title
    try:
        for i in range(len(df)):
            if i == 0 and target_time <= df.loc[i, "datetime"]:  # 如果时间戳对应的是第一条记录，直接返回该记录的window_title
                return df.loc[i, "window_title"]
            elif target_time >= df.loc[i, "datetime"] and target_time < df.loc[i + 1, "datetime"]:  # 如果时间戳对应的记录在中间
                # 如果时间早于下一条记录1秒则返回上一条记录的window_title
                if df.loc[i + 1, "datetime"] - target_time < datetime.timedelta(seconds=1):
                    return df.loc[i + 1, "window_title"]
                else:  # 否则返回当前记录的window_title
                    return df.loc[i, "window_title"]
            elif i == len(df) - 1 and target_time >= df.loc[i, "datetime"]:  # 如果时间戳对应的是最后一条记录，直接返回该记录的window_title
                return df.loc[i, "window_title"]
    except (ValueError, KeyError) as e:
        print(e)
        pass

    return None


def optimize_wintitle_name(text):
    """根据特定策略优化页面名字"""
    text = str(text)

    # telegram: 只保留对话名
    # eg. "(1) 大懒趴俱乐部 – (283859)"
    text = re.sub(" – \\(\\d+\\)", "", text)  # 移除最后的总未读消息
    text = re.sub(" - \\(\\d+\\)", "", text)
    text = re.sub("^\\(\\d+\\) ", "", text)  # 移除最开始的当前对话未读消息

    return text


# 获取当天前台窗口标题统计情况
def get_wintitle_stat_in_day(dt_in: datetime.datetime):
    df = OneDay().search_day_data(dt_in, search_content="")
    # 在生成前清洗数据：
    # from windrecorder import record_wintitle
    # df["win_title"] = df["win_title"].apply(record_wintitle.optimize_wintitle_name)
    df.sort_values(by="videofile_time", ascending=True, inplace=True)
    df = df.reset_index(drop=True)
    stat = {}
    for index, row in df.iterrows():
        win_title_name = str(row["win_title"])
        if win_title_name == "None" or win_title_name == "nan":
            continue
        if win_title_name not in stat:
            stat[win_title_name] = 0
        if index == df.index.max():
            break
        second_interval = df.loc[index + 1, "videofile_time"] - df.loc[index, "videofile_time"]
        if second_interval > 100:  # 添加阈值，排除时间差值过大的 row，比如隔夜、锁屏期间的记录等
            second_interval = 100
        stat[win_title_name] += second_interval

    # 清洗整理数据
    stat = {key: val for key, val in stat.items() if val > 1}
    df_show = pd.DataFrame(list(stat.items()), columns=["Page", "Screen Time"])
    df_show.sort_values(by="Screen Time", ascending=False, inplace=True)
    df_show = df_show.reset_index(drop=True)
    df_show["Screen Time"] = df_show["Screen Time"].apply(utils.convert_seconds_to_hhmmss)

    return df_show


# ------------streamlit component
# 窗口标题组件
def component_wintitle_stat(day_date_input):
    day_wintitle_df_statename_date = day_date_input.strftime("%Y-%m-%d")
    day_wintitle_df_statename = f"wintitle_stat_{day_wintitle_df_statename_date}"
    if day_wintitle_df_statename not in st.session_state:
        st.session_state[day_wintitle_df_statename] = get_wintitle_stat_in_day(day_date_input)
    if len(st.session_state[day_wintitle_df_statename]) > 0:
        st.dataframe(
            st.session_state[day_wintitle_df_statename],
            column_config={"Page": st.column_config.TextColumn(_t("oneday_wt_text"), help=_t("oneday_wt_help"))},
            height=650,
            hide_index=True,
            use_container_width=True,
        )
    else:
        st.markdown(_t("oneday_ls_text_no_wintitle_stat"), unsafe_allow_html=True)
