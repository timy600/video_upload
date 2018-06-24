from moviepy.editor import *
import os

class VideoHelper(object):
    @staticmethod
    def convert(video_input, video_output_name, width=None, height=None):
        if width is not None and height is not None:
            clip = VideoFileClip(video_input, audio=True, target_resolution=[height, width])
        else:
            clip = VideoFileClip(video_input, audio=True)
        w, h = clip.size  # size of the clip
        logo = VideoHelper.get_watermark(clip.duration, w, h)

        final = CompositeVideoClip([clip, logo])
        final.duration = clip.duration
        final.write_videofile(video_output_name, codec='libx264')

    @staticmethod
    def get_watermark(duration, width, height):
        return (ImageClip(os.path.dirname(__file__) + "/../assets/watermark/watermark.png")
                .set_duration(duration)
                .resize(height=int((15/100) * height)) # if you need to resize...
                .margin(right=int((5/100) * width), top=int((5/100)*height), opacity=0) # (optional) logo-border padding
                .set_pos(("right", "top")))

