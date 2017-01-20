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

## References
http://docs.getpelican.com/en/stable/settings.html

## Elegant Theme
https://github.com/tshepang/tshepang.github.com
http://oncrashreboot.com/elegant-best-pelican-theme-features#home-page-features