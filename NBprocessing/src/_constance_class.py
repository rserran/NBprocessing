"""
constance file, generate all constance values from json file
"""

from NBprocessing.src._constance_dict import data


class Const(object):
    def __init__(self):

        # check input file
        self.CHECK_DATABASE_INPUT = data["CHECK_INPUT"]["CHECK_DATABASE_INPUT"]
        self.CHECK_COLUMN_NAME = data["CHECK_INPUT"]["CHECK_COLUMN_NAME"]
        self.CHECK_COLUMN_IN_DATABASE = data["CHECK_INPUT"]["CHECK_COLUMN_IN_DATABASE"]
        self.CHECK_LIST_TUPLE_NONE = data["CHECK_INPUT"]["CHECK_LIST_TUPLE_NONE"]
        self.CHECK_THRESHOLD = data["CHECK_INPUT"]["CHECK_THRESHOLD"]
        self.CHECK_TYPE_DATE_TIME = data["CHECK_INPUT"]["CHECK_TYPE_DATE_TIME"]
        self.CHECK_BOUNDARIES = data["CHECK_INPUT"]["CHECK_BOUNDARIES"]
        self.CHECK_DICT = data["CHECK_INPUT"]["CHECK_DICT"]
        self.CHECK_NUM_CATEGORIES = data["CHECK_INPUT"]["CHECK_NUM_CATEGORIES"]
        self.CHECK_TITLE = data["CHECK_INPUT"]["CHECK_TITLE"]

        # categorical
        self.RED = data["CATEGORICAL"]["GENERAL_FUNCTIONS_CATEGORICAL"]["RED"]
        self.BLACK = data["CATEGORICAL"]["GENERAL_FUNCTIONS_CATEGORICAL"]["BLACK"]
        self.OUTPUT = data["CATEGORICAL"]["GENERAL_FUNCTIONS_CATEGORICAL"]["OUTPUT"]
        self.USER_INPUT = data["CATEGORICAL"]["NBCATEGORICAL_CLASS"]["REMOVE_CATEGORIES"]["USER_INPUT"]
        self.DATABASE_SHAPE = data["CATEGORICAL"]["NBCATEGORICAL_CLASS"]["REMOVE_CATEGORIES"]["DATABASE_SHAPE"]
        self.FIRST = data["CATEGORICAL"]["NBCATEGORICAL_CLASS"]["CATEGORIES_NOT_IN_COMMON"]["FIRST"]
        self.SECOND = data["CATEGORICAL"]["NBCATEGORICAL_CLASS"]["CATEGORIES_NOT_IN_COMMON"]["SECOND"]

        # continues
        self.DROP_ROW = data["CONTINUOUS"]["NBCONTINUOUS_CLASS"]["REMOVE_OUTLIERS_BY_BOUNDARIES"]["DROP_ROW"]
        self.TYPE_ERROR = data["CONTINUOUS"]["NBCONTINUOUS_CLASS"]["REMOVE_OUTLIERS_BY_BOUNDARIES"]["TYPE_ERROR"]
        self.OUTLIERS_ABOVE = data["CONTINUOUS"]["NBCONTINUOUS_CLASS"]["GET_NUM_OUTLIERS_BY_VALUE"]["OUTLIERS_ABOVE"]
        self.SUM_OUTLIERS_ABOVE = data["CONTINUOUS"]["NBCONTINUOUS_CLASS"]["GET_NUM_OUTLIERS_BY_VALUE"] \
            ["SUM_OUTLIERS_ABOVE"]
        self.OUTLIERS_UNDER = data["CONTINUOUS"]["NBCONTINUOUS_CLASS"]["GET_NUM_OUTLIERS_BY_VALUE"] \
            ["OUTLIERS_UNDER"]
        self.SUM_OUTLIERS_UNDER = data["CONTINUOUS"]["NBCONTINUOUS_CLASS"]["GET_NUM_OUTLIERS_BY_VALUE"] \
            ["SUM_OUTLIERS_UNDER"]
        self.SUM_OUTLIERS_TOT = data["CONTINUOUS"]["NBCONTINUOUS_CLASS"]["GET_NUM_OUTLIERS_BY_VALUE"] \
            ["SUM_OUTLIERS_TOT"]
        self.KEY_ERROR = data["CONTINUOUS"]["NBCONTINUOUS_CLASS"]["GET_NUM_OUTLIERS_BY_VALUE"]["KEY_ERROR"]
        self.SHAPE_BEFORE = data["CONTINUOUS"]["NBCONTINUOUS_CLASS"]["REMOVE_OUTLIERS_BY_VALUE"]["SHAPE_BEFORE"]
        self.SHAPE_AFTER = data["CONTINUOUS"]["NBCONTINUOUS_CLASS"]["REMOVE_OUTLIERS_BY_VALUE"]["SHAPE_AFTER"]
        self.DATA_LOST = data["CONTINUOUS"]["NBCONTINUOUS_CLASS"]["REMOVE_OUTLIERS_BY_VALUE"]["DATA_LOST"]

        # plot
        self.NULL_HEAT_MAP_TITLE = data["PLOT"]["NBPLOT_CLASS"]["NULL_HEAT_MAP_TITLE"]
        self.FEATURE_CORR = data["PLOT"]["NBPLOT_CLASS"]["FEATURE_CORR"]
