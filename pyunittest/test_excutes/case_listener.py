from ddt import file_data, ddt


@ddt
class caseListener:
    def method_automation(self,dict_info):
        # @file_data("./test_app_dict.json")
        # @file_data("./Test_Data/ServicePatrol_dict.json")
        def _deco(func):
            def __deco(*args, **kwargs):
                #打印测试描述
                print(kwargs["des"])
                try:
                    print(' ')
                    # print(kwargs["temprespons"])
                except Exception as e:
                    print(e, 'error')
                func(*args, **kwargs)
            return __deco
        return _deco