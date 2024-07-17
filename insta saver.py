#pip install instaloader
import instaloader
ig=instaloader.Instaloader()
dp=input()
ig.download_profile(dp,profile_pic_only=True)