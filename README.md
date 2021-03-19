# Google Drive Uploader
This simple wrapper library of [PyDrive2](https://github.com/iterative/PyDrive2)
that upload or update your files from command `git status` to yout Google Drive.

## Authentication with PyDrive2
The first step you should definitelly do is Drive API authentication. You can
visit the oficial documentation
[here](https://iterative.github.io/PyDrive2/docs/build/html/quickstart.html#authentication)
or just follow the steps below.

1. Visit the [Google Cloud platform](https://console.cloud.google.com) and make
a new project
2. In navigation menu search for `API & Services` then `Library` (or just click [here](https://console.cloud.google.com/apis/library?project=python-uploader-307110))
3. Look for the `Google Drive API` and then click `Enable`
4. Back in the navigation menu select `API & Services` then `Credentials`
5. Click `+ Create credentials`, select `OAuth client ID`.
    * Select ‘Application type’ to be Web application.
    * Enter an appropriate name.
    * Input http://localhost:8080/ for ‘Authorized redirect URIs’.
    * Click ‘Create’
6. You should download the `JSON` file (with download button on the right side)
7. The downloaded file has all the authentication information of your new project
8. Rename the `JSON` file to `client_secrets.json`

## Create alias
For better interaction create alias for the commad `git status -sb > status_out.txt`
(if you are `bash` user):
```bash
echo -e "# My custom aliases\nalias gso='git status -sb > status_out.txt'" > ~/.bash_aliases
```

## Running script
Install the dependency file first:
```bash
pip install -r requirements.txt
```
Then run the file with argument. The argument should be path to your projects.
The script searches for a file `status_out.txt` by default.
