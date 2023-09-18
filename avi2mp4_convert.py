import moviepy.editor as moviepy

clip = moviepy.VideoFileClip("myvideo.avi")
clip.write_videofile("myvideo.mp4")