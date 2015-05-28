.. title: Extracting public key from pem file
.. slug: extracting-public-key-from-pem-file
.. date: 2015-05-28 11:52:28 UTC+05:30
.. tags: automation, pki
.. category: 
.. link: 
.. description: Extracting public key from a pem file
.. type: text

If you need to extract the public key from your `PEM`_ format certificate file, you can use
the ``ssh-keygen`` command for this like so:

.. code-block:: bash
                
   ssh-keygen -f certificate.pem -y

where ``certificate.pem`` is your pem file. This command will output the public key
on ``stdout``.
                


.. _`PEM`: http://en.wikipedia.org/wiki/Privacy-enhanced_Electronic_Mail
