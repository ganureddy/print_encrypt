## Print Encrypt

<p align="center">
  Print Encrypt
</p>

<hr>

 Print Encrypt is a software tool designed to enhance security by encrypting sensitive information before sending email, utilizing a password-based mechanism to safeguard Attachment documents in [ERPNext](https://erpnext.com) and Frappe.

<hr>

## Features

1. use Notification doctype to trigger emails This is core feature that Frappe has already Build. 
1. Encrypt attachement 📑 using 
Encrypt print field.
2. Set Password Policy.

    <b>Example:</b> SO-{{doc.name}}<br>This will generate a password like SO-SAL-ORD-2023-00001.

<hr>

## Tech Stack

This app is built using the [Frappe Framework](https://frappeframework.com) - an open-source full stack development framework. 

These are some of the tools it's built on:
- [Python](https://www.python.org)
<br>


<details>
  <summary>Show more screenshots</summary>
  

 
<p align="center">
    <figure>
        <img width="1402" src="print_encrypt/public/Screenshot from 2024-01-28 23-53-14.png" alt="Private Channel" />
         <figcaption align="center">
            <b>attachement Secure and Password based</b>
        </figcaption>
    </figure>
</p>

</details>



## Installation

Since Print Encrypt is a Frappe app, it can be installed via [frappe-bench](https://frappeframework.com/docs/v14/user/en/bench) on your local machine or on your production site.

Once you have [setup your bench](https://frappeframework.com/docs/v14/user/en/installation) and your [site](https://frappeframework.com/docs/v14/user/en/tutorial/install-and-setup-bench), you can install the app via the following commands:

```bash
bench get-app https://github.com/ganureddy/print_encrypt.git
bench --site yoursite.name install-app print_encrypt
```



## License

MIT