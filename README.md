# tiktok-archiver
A docker image that downloads all the videos/photos on a tiktok account then uploads them to the internet archive. It will then run the same proccess again archiving the videos in real time whilst avoiding redownloading the videos you already have.
<hr>
Under the hood the repo uses two of my other repositorys to do its work the https://github.com/jgore077/Internet-Archive-Uploader and https://github.com/jgore077/tiktok-downloader. The base is Ubuntu as I need to run both Python and Node.js code.

# Usage
This repo requires quite a bit of extra information to run such as your cookies for TikTok, an Internet Archive email & password, and a few other enviroment variables. The cookies are required for the link gathering because TikTok wont load videos without them. All these enviroment variables need to be set in order for the container to work regardless of whether you are running a complete container or `docker compose`

## Cookies (<b>IMPORTANT!</b>)
Unfortunately due to the design of my TikTok downloader you will need to pass a `cookies.json` file into the container in order to get it to work. This is a huge drawback to this project as it increases the complexity of the setup. In future work I may be able to get private downloads working (requires cookies) but If I cant I will look for another solution.
<hr>

To get these cookies clone https://github.com/jgore077/tiktok-downloader and follow its instructions. Once you have the cookies, run this command in the the `tiktok-downloader` directory.
```
docker cp cookies.json <Container name>:app
```
Once you have copied these cookies the container will run as intended.

## Configuring the .env file (docker compose)

The `IDENTIFIER` must be 100% unique or else it will cause conflicts with the Internet Archive. You can perform and advanced search with your `IDENTIFIER` at [https://archive.org/advancedsearch.php](https://archive.org/advancedsearch.php) to verify it is not in use. If you have any questions about these variables open an issue and I will explain it.

```
IDENTIFIER= <A unique archive.org identifier that refers to your collection uniquely>
USER= <The username of the TikTok user you want to archive (e.g., therock,rihanna,brainiacsosmart)>
IA_USERNAME= <The email of your archive.org account>
IA_PASSWORD= <The password to your archive.org account>
SUBJECT= <A list of comma separated values (a singlular value is also ok) that will be in the subject of the archive>
CREATOR=<The creator of the content>
DESCRIPTION= <A short description to give information about the archive>
```
## Example .env file
```
IDENTIFIER=therockarchive
USER=therock
IA_USERNAME=example@gmail.com
IA_PASSWORD=internetarchivepassword
SUBJECT=the rock, dwayne johnson, tik tok
CREATOR=The Rock
DESCRIPTION=This is an archive of the @therock's TikTok account
```
