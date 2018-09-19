# Django 1.11 on Digital Ocean

* Set up a new account and pick the cheapest ($5) droplet. The OS and Django version are fixed (1.11)

* I set up a SSH key locally but didn't notice the root password, so I reset it through the admin panel

* The site, by default, seems to be accessible only through its IP address.

* how to restart app: [Official tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)

```
sudo systemctl restart gunicorn
```

* If gunicorn's systemd service file is changed:

```
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```

## Questions

* https access?
