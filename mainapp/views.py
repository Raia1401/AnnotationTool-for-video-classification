import glob
import os
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from natsort import natsorted


START_VIDEO_NUMBER=0
VIDEO_PATH_LIST=natsorted(glob.glob(settings.ANNOTATION_DATA_DIR+'/*.mp4'))
VIDEO_COUNT= len(VIDEO_PATH_LIST)


def make_answer_file():
    now = datetime.datetime.now()
    answer_file_name='answer/answer_'+ now.strftime('%Y%m%d_%H%M%S')+'.txt'
    f = open(answer_file_name, 'x')
    f.close()
    return answer_file_name


def save_answer_file(answer_file_name,answer_contents):
    f = open(answer_file_name, 'a')
    answer_text=''
    for answer_content in answer_contents:
        if answer_content != answer_contents[-1]:
            answer_text += (str(answer_content)+' ')
        else: #最後のコンテントには改行を入れておく
            answer_text += (str(answer_content)+'\n')
    f.write(answer_text)
    f.close()


def index(request):
    video_number=0
    template = loader.get_template('video.html')

    #ボタンが押された時に以下の処理をする
    if request.method == 'POST':

        video_number=int(request.POST['video_number'])
        video_path=VIDEO_PATH_LIST[video_number]
        video_name=os.path.basename(video_path)

        #入力データを保存する
        answer_file_name=request.POST['answer_file_name']
        answer=request.POST['q']
        answer_contents=[video_number,video_name,answer] #保存したい入力内容はこのリストに入れる
        save_answer_file(answer_file_name,answer_contents)

        video_number+=1

        #最後のページを表示する場合
        if video_number == VIDEO_COUNT:
            context={}
            template=loader.get_template('end_page.html')
            return HttpResponse(template.render(context, request))

        #最後のページ以外を表示する場合
        else:
            next_video_path=VIDEO_PATH_LIST[video_number]
            next_video_name=os.path.basename(next_video_path)

            context = {'video_name':next_video_name,'video_number':video_number,\
                       'video_count':VIDEO_COUNT,'answer_file_name':answer_file_name}

            return HttpResponse(template.render(context, request))

    #最初にアクセスした時
    else:
        answer_file_name=make_answer_file()

        video_number=START_VIDEO_NUMBER
        video_path=VIDEO_PATH_LIST[video_number]
        video_name=os.path.basename(video_path)


        context = {'video_name':video_name,'video_number':video_number,\
                   'video_count':VIDEO_COUNT,'answer_file_name':answer_file_name}
                   #'collision_time':collision_time}

        return HttpResponse(template.render(context, request))


 #TODO:GETが発動すると最初のページに戻ってしまうことの対応（URLに触れたりリロードすると問題が発生する）
