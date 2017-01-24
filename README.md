# Do everything regarding the changes in blog, do everything
# at the source branch
# To publish locally
make html && make serve
# check on http://localhost:8000/:

# To publish (i.e. update the remote branch master)
# git checkout source
# ghp-import -b master output/
# git push origin master
make github

---
# 2017-01-06
# New workflow
# Interactive (updates when there is a modification)
make regenerate&
make serve
# check on localhost:8000

# Whenever you want to see the changes on the actual website
make github
# open cocoaaa.github.io/blog on the browser

# Before finishing up the session, save all the changes of source
git branch #check if you are on the source branch
git commit -am "message"
git push origin source

---
#2017-01-24 
#Yet another workflow. See updated Makefile
make html: writes content/ to output/ using local config
make publish: writes content/ to output/ using remote config
(Note: whether to delete output/ everytime remote conf is used
        is set in the publishconf.py)
make clean: deletes the output folder
make github: 1) make sure I'm in the source branch
             2) upload source branch's output/ to master branch's output/
             3) push the local output/ in master branch to the remote branch

#summary
to publish to the remote server do in the source branch:
1) make clean && make publish 
(!CAUTION: this deletes all the old files not in the current output folder)
                        
2) make github

or. 
1)make html && make github


## References
http://docs.getpelican.com/en/stable/settings.html

## Elegant Theme
https://github.com/tshepang/tshepang.github.com
http://oncrashreboot.com/elegant-best-pelican-theme-features#home-page-features