#案例一：默认“#”
# import time
# from progressbar import *
# class Exmple1():
#     def dosomthing(self):
#         progress = ProgressBar()
#         for i in progress(range(1000)):
#             time.sleep(0.01)
#
# if __name__ == '__main__':
#     m = Exmple1()
#     m.dosomthing()

#案例二
# import  time
# from progressbar import *
# total = 1000
# def dosomework():
#     time.sleep(0.01)
# # widgets = ['Progress: ',Percentage(), ' ', Bar('#'),' ', Timer(),' ', ETA(), ' ', FileTransferSpeed()]
# #Bar的符号，可以自定义，这是黑白的
# widgets = ['进度: ',Percentage(), ' ', Bar('>'),' ', Timer(),' ', ETA(), ' ', FileTransferSpeed()]
# #颜色，可自定义：彩色：依次是36,35,34,33,32,31
#
# pbar = ProgressBar(widgets=widgets, maxval=10*total).start()
# for i in range(total):
#     # do something
#     pbar.update(10 * i + 1)
#     dosomework()
# pbar.finish()

#案例三
# import  time
# import progressbar
# #自定义
# widgets = [
#     'Colorful example',
#     progressbar.Percentage(),
#     progressbar.Bar(marker='='),
# ]
# bar = progressbar.ProgressBar(widgets=widgets, max_value=100).start()
# for i in range(100):
#     # do something
#     time.sleep(0.1)
#     bar.update(i + 1)
# bar.finish()

#案例四
import  time
import progressbar
widgets = [
    '进度：',
    progressbar.Percentage(),
    progressbar.Bar(marker=progressbar.AnimatedMarker(
        #可自定义：fill='x',
        fill='█',
        fill_wrap='{}',
        marker_wrap='{}',
    )),
]
bar = progressbar.ProgressBar(widgets=widgets, max_value=100).start()
for i in range(100):
    # do something
    time.sleep(0.1)
    bar.update(i + 1)
bar.finish()