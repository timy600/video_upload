import pafy

video = pafy.new("d7RWIcOcHgg")
t = video.title
r = video.rating
print(t)
print(r)
best = video.getbest("mp4")
filename = best.download(quiet = False)
