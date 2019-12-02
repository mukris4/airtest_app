from airtest.cli.runner import AirtestCase, run_script
from argparse import *
import airtest.report.report as report
import jinja2
import shutil
import os
import io
import datetime

class CustomAirtestCase(AirtestCase):
    def setUp(self):
        print("custom setup")

        super(CustomAirtestCase, self).setUp()

    def tearDown(self):
        print("custom tearDown")
        super(CustomAirtestCase, self).setUp()

    def run_air(self, root_dir='C:\\Users\\dbk\\AppData\\Local\\Programs\\Python\\Python35\\airtestCase\\case', device=['android://127.0.0.1:5037/127.0.0.1:7555']):
        # 聚合结果
        results = []
        # 获取所有用例集
        root_log = root_dir + '\\' + 'log'
        if os.path.isdir(root_log):
            shutil.rmtree(root_log)
        else:
            os.makedirs(root_log)
            print(str(root_log) + 'is created')

        for f in os.listdir(root_dir):
            if f.endswith(".air"):

                airName = f
                script = os.path.join(root_dir, f)

                print(script)
                now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-')

                log = os.path.join(root_dir, 'log' + '\\' + airName.replace('.air', ''))
                print(log)
                if os.path.isdir(log):
                    shutil.rmtree(log)
                else:
                    os.makedirs(log)
                    print(str(log) + 'is created')
                output_file = log + '\\' + 'log.html'
                args = Namespace(device=device, log=log, recording=None, script=script)
                try:
                    run_script(args, AirtestCase)
                except:
                    pass
                finally:
                    rpt = report.LogToHtml(script, log)
                    rpt.report("log_template.html", output_file=output_file)
                    result = {}
                    result["name"] = airName.replace('.air', '')

                    result["result"] = rpt.test_result
                    results.append(result)
        # 生成聚合报告
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(root_dir),
            extensions=(),
            autoescape=True
        )

        template = env.get_template("summary_template.html", log)
        html = template.render({"results": results})
        output_file = os.path.join(root_dir, now+"-summary.html")
        with io.open(output_file, 'w', encoding="utf-8") as f:
            f.write(html)
        print(output_file)


if __name__ == '__main__':
    test = CustomAirtestCase()
    device = ['android://127.0.0.1:5037/127.0.0.1:7555']
    test.run_air('C:\\Users\\dbk\\AppData\\Local\\Programs\\Python\\Python35\\airtestCase\\case', device=['android://127.0.0.1:5037/127.0.0.1:7555'])


