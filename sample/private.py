# this file is imported from src/private.py


class PrivateFunc:
    __slots__ = ["_filename", "__error_name", "__error_message"]
    __version__ = '1.2.21'
    _filename: str
    __error_name: type
    __error_message: str
    def __init__(
            self,
            filename,  # name of the file, where the object of PrivateFunc class is created
            error_name="",  # name of the error which will be raised if private function is called illegally
            error_message=""  # message that will be shown with the error name
            # filename is a default parameter, error_name and error_message are non-default parameters
    ):
        self._filename = filename
        try:
            if error_name:
                self.__error_name = error_name
            else:
                self.__error_name = ImportError
        except Exception:
            self.__error_name = ImportError
        self.__error_message = error_message

    def private(self, func):
        from sys import argv
        from inspect import stack
        import os.path as path
        def wrap(*args, **kwargs):
            if self._filename != argv[0]:
                caller_file_module = stack()[1].filename
                caller_file_module = path.splitext(path.basename(caller_file_module))[0]
                if self._filename != caller_file_module:
                    if not self.__error_message:
                        raise self.__error_name(
                            "cannot import " + func.__name__ + " from " + self._filename
                            + " because it is a private function")
                    else:
                        raise self.__error_name(self.__error_message)
            func(*args, **kwargs)
        return wrap
