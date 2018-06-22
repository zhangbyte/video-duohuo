#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ffmpy import FFmpeg
import os


def get_screenshot(video):
    # 暂存文件
    video.save(os.path.join('tmp', video.filename))

    ff = FFmpeg(
        inputs={get_tmp_video_path(video.filename): None},
        outputs={get_tmp_img_path(video.filename): '-y -f image2 -ss 1 -t 0.001'}
    )

    ff.run()


def get_tmp_img_path(video_name):
    return 'tmp/{0}.jpg'.format(video_name.rsplit('.', 1)[0])


def get_tmp_video_path(video_name):
    return 'tmp/{0}'.format(video_name)
