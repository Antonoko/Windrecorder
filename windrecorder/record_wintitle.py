# 记录活动前台的窗口标题名
import datetime
import os

import pandas as pd
import pygetwindow

from windrecorder import file_utils, utils
from windrecorder.config import config
from windrecorder.db_manager import db_manager

CSV_TEMPLATE_DF = pd.DataFrame(columns=["datetime", "window_title"])
window_title_last_record = ""


def get_csv_filepath(datetime: datetime.datetime):
    """取得对应 datetime 的 wintitle csv 路径，如不存在则返回 None"""
    csv_filename = datetime.strftime("%Y-%m-%d") + ".csv"
    csv_filepath = os.path.join(config.win_title_dir, csv_filename)
    return csv_filepath


def record_wintitle_now():
    """记录当下的前台窗口标题到 csv"""
    global window_title_last_record
    windowTitle = str(pygetwindow.getActiveWindowTitle())

    # 如果与上次检测结构一致，则跳过
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

    return None


def get_statistics_in_day(dt_in: datetime.datetime):
    search_date_range_in = dt_in.replace(hour=0, minute=0, second=0, microsecond=0)
    search_date_range_out = dt_in.replace(hour=23, minute=59, second=59, microsecond=0)
    df, _, _ = db_manager.db_search_data("", search_date_range_in, search_date_range_out)
