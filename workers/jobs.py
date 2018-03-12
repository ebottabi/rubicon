#!/usr/bin/python
import sys

sys.path.append("../")
import tornado
import json
from core.utils.libsmq import JSONGearmanWorker
from core import app
from flask import current_app
import logging
from logging.config import dictConfig

logging_config = dict(
    version=1,
    formatters={
        'f': {'format':
                  '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
    },
    handlers={
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG}
    },
    loggers={
        'root': {'handlers': ['h'],
                 'level': logging.DEBUG}
    }
)

dictConfig(logging_config)
logger = logging.getLogger(__name__)


class JobsHelper(object):
    def __init__(self):
        self._urls = list()
        self._gm_job = None
        self._gm_worker = JSONGearmanWorker(['localhost:4730'])
        self._gm_worker.register_task('csv.clean', self._clean_csv)
        try:
            logger.info('Background job workers initialized and ready for work')
            self._gm_worker.work()
        except KeyboardInterrupt:
            logger.info('Exiting')
            pass
        except Exception, e:
            logger.error('Exiting - %s' % e)

    def _clean_csv(self, gm_worker, gm_job):
        data = json.loads(gm_job.data)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    JobsHelper()
