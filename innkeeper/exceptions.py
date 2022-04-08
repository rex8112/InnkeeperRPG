class InnkeeperError(Exception):
    pass

class NotFoundError(InnkeeperError):
    pass

# Item Exceptions
class ItemError(InnkeeperError):
    pass

class UnstackableError(ItemError):
    pass