# coding=utf8


class Config(object):
    """这里是公共配置信息类"""

    SQLALCHEMY_ECHO = True # 翻译成SQL语句并把他打印出来
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class PrdConfig(Config):
    """生产环境"""


class TestConfig(Config):
    """开发测试环境"""


class DevConfig(Config):
    """本地开发环境"""
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://XXXX:XXXX@127.0.0.1:3306/victoria?charset=utf8'


config = {
    'development': DevConfig,
    'test': TestConfig,
    'production': PrdConfig
}