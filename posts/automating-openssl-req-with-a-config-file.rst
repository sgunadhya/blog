.. title: Automating openssl req with a config file
.. slug: automating-openssl-req-with-a-config-file
.. date: 2015-05-26 08:14:10 UTC+05:30
.. tags: openssl, automation, pki
.. category: automation
.. link: 
.. description: Automate openssl req using a config file
.. type: text

The other day I was trying to generate a Certificate Signing Request using the ``openssl`` command
. The `openssl`_ command supports `a lot of`_ commands, and if you are like me, you always have difficulty
remembering them.

``req``, ``x509`` and ``ca`` commands from ``openssl`` support providing options using
an INI-style configuration file. The config file option is useful when running ``openssl``
commands in batch mode. The batch mode operation saves time  when you are trying to automate a series of steps using bash,
one of which involves using the ``opnessl`` command to generate a CSR or sign a certificate.

Let us suppose you want to generate a CSR for your server. You use a command like so:

.. sourcecode:: bash
   
   openssl req -nodes -new -newkey rsa:2048 -out orom-staging.in.csr -keyout orom-staging.in.key

You will then enter an interactive mode where you will need to enter details like
Country, Organization Unit etc.

To automate this, you can create a INI-style config file ``csr.conf`` like so:

.. sourcecode:: INI
                
  [req]
  default_bits = 2048
  default_ketfile = $ENV::SERVER.key
  distinguished_name = req_distinguished_name

  [req_distinguished_name]
  countryName = Country Name (2 letter coe)
  countryName_default = IN
  stateOrProvineName_default = KA
  organizationName_default = Orom
  organizationalUniteName_default = Engineering
  commonName_default = $ENV::SERVER
  emailAddress_default = ssushant@orom.in

You can then generate your CSR like so:

.. code-block:: bash
                
   SERVER=www.orom-staging.in openssl req -nodes -config csr.conf -out orom-staging.in.csr

.. _`openssl`: https://www.openssl.org
.. _`a lot of`: https://www.openssl.org/docs/apps/openssl.html
