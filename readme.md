# Caesar Message Encryption (Daisi Hackathon)
Python function as a web service to Encrypt & Decrypt text message using **Caesar cipher** algorithm.

### Example
<pre>
message = "Hello World!"
</pre>
We will encrypt this message using key `k=6` which is fixed right shift rotations of the alphabet characters 
<pre>
caesarCipher_encode(message, 6)
</pre>
The encrypted message : `Nkrru Cuxrj!`

To decrypt the message we use the exact key `k=6` in reverse which is left shift rotations of the characters.
<pre>
caesarCipher_decode(encrypted_msg, 6)
</pre>
`Hello World!`
### How to call it

* Load the Daisi
<pre>
import pydaisi as pyd
caesar_message_encryption = pyd.Daisi("oghli/Caesar Message Encryption")
</pre>

* Call the `caesar_message_encryption` end point, passing the text message and the key of Caesar cypher
<pre>
msg = "Hello World!"
encrypted_msg = caesar_message_encryption.caesarCipher_encode(msg, 6).value
encrypted_msg
</pre>

* Finally, it will return the encrypted message

  `Nkrru Cuxrj!`

To decrypt the message we can call the function `caesarCipher_decode(en_msg, k)` from the end point:
<pre>
decrypted_msg = caesar_message_encryption.caesarCipher_decode(encrypted_msg, 6).value
decrypted_msg
</pre>
`Hello World!`

To display transformation table of Caesar cypher for the key `k=6 ` we can call function `get_cypher_table(k)` from the end point:
<pre>
cypher_table = caesar_message_encryption.get_cypher_table(6).value
cypher_table
</pre>
It will print:
<pre>
{
    'Plain': 'Cypher',
    'A': 'G',
    'B': 'H',
    'C': 'I',
    'D': 'J',
    'E': 'K',
    'F': 'L',
    'G': 'M',
    'H': 'N',
    'I': 'O',
    'J': 'P',
    'K': 'Q',
    'L': 'R',
    'M': 'S',
    'N': 'T',
    'O': 'U',
    'P': 'V',
    'Q': 'W',
    'R': 'X',
    'S': 'Y',
    'T': 'Z',
    'U': 'A',
    'V': 'B',
    'W': 'C',
    'X': 'D',
    'Y': 'E',
    'Z': 'F'
}
</pre>


For more info about Caesar cipher check this reference:

https://en.wikipedia.org/wiki/Caesar_cipher
