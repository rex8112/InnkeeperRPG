import threading
import datetime


class SnowflakeGenerator:
    start_date = datetime.datetime(2022, 1, 1, tzinfo=datetime.timezone.utc)

    def __init__(self, worker_id: int) -> None:
        self.worker_id = worker_id
        self.id_counter = 0
        self.id_counter_lock = threading.Lock()
        self.id_counter_lock.acquire()
        self.id_counter_lock.release()

    #Static methods
    @staticmethod
    def get_datetime_from_id(id: int) -> datetime.datetime:
        time_since_start = id >> 22
        return SnowflakeGenerator.start_date + datetime.timedelta(seconds=time_since_start)

    #Methods
    def get_new_id(self) -> int:
        """Returns a new unique id.
        
        Binary format:
        [63-22] Seconds since epoch+1640995200
        [21-17] Worker id
        [16-0] Id counter"""
        self.id_counter_lock.acquire()

        count = self.id_counter
        self.id_counter += 1
        first = self.get_time_since_start() << 22
        second = self.worker_id << 17
        third = count

        new_id = first | second | third

        self.id_counter_lock.release()
        return new_id

    def get_time_since_start(self) -> int:
        return int((datetime.datetime.now(datetime.timezone.utc) - self.start_date).total_seconds())