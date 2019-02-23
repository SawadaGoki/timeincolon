
import inspect
# t = TimeInColon("10:00")

# t + "2:11"
# t - "13:11"

class test:
    def __init__(self):
        self.name = 

    def _retrieve_name(self, var):
        """
        Gets the name of var. Does it from the out most frame inner-wards.
        :param var: variable to get name from.
        :return: string
        """
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            for var_name, var_val in fi.frame.f_locals.items():

                print("-------------------------------")
                print(var_name)
                print("-------------------------------")
            if len(names) > 0:
                return names[0]

taa = test()

print(taa.name)