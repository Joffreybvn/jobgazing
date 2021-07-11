
from typing import Union
from . import Job, Enterprise


class Database:

    def __init__(self):
        pass

    def get_enterprise(self, job_type: Union[Job.AI, Job.WEB]):

        return Enterprise(
            name='Radix',
            locations=['Brussels'],
            website='https://radix.ai'
        )

