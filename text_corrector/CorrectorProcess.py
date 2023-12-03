from pycorrector import Corrector
import pycorrector

class EmailHelper(Corrector):

    # translate traditional Chinese to simplified Chinese
    def tra2sim(self, content):
        try:
            sim_content = pycorrector.traditional2simplified(content.replace("\n", '').replace(" ", ''))
            return [sim_content]
        except:
            sim_content = [pycorrector.traditional2simplified(tra_content.replace("\n", '').replace(" ", '')) for tra_content in content]
            return sim_content

    # get the values which the key equals to "target"
    def get_target(self, correct_dict):
        if len(correct_dict) == 1:
            self.error = correct_dict[0]["errors"]
            return correct_dict[0]["target"]
        else:
            self.error = [f"第{i+1}篇錯誤：{j['errors']}" for i, j in enumerate(correct_dict)]
            return [i["target"] for i in correct_dict]


    # translate traditional Chinese to simplified Chinese
    def sim2tra(self, content):
        if type(content) == str:
            tra_content = pycorrector.simplified2traditional(content)
        else:
            tra_content = [pycorrector.simplified2traditional(sim_content) for sim_content in content]
        return tra_content