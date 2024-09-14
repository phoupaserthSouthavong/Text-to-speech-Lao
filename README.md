# Text-to-speech-Lao 
 Text to speech Lao 


Key Features:
Extracting the First Paragraph: The function get_first_paragraph splits the text into paragraphs using two consecutive newlines (\n\n). The first paragraph is selected.

Filename Sanitization: The sanitize_filename function removes characters that are illegal in filenames, such as \/:*?"<>|. This ensures that the extracted text can be safely used as a file name.

Filename Limitation: The output file name is limited to the first 50 characters of the paragraph to avoid overly long file names.

Voice Selection: The script still allows switching between male and female voices based on the use_male_voice toggle.

Output:
Audio File Name: The first 50 characters of the first paragraph from the text file will be used as the output MP3 file name.
This should meet your need for extracting the first paragraph and using it as the output file name.


ຄຸນ​ນະ​ສົມ​ບັດ​ທີ່​ສໍາ​ຄັນ​:
ການສະກັດຫຍໍ້ໜ້າທຳອິດ: ຟັງຊັນ get_first_paragraph ແຍກຂໍ້ຄວາມອອກເປັນວັກໂດຍໃຊ້ແຖວໃໝ່ສອງແຖວຕິດຕໍ່ກັນ (\n\n). ວັກທໍາອິດຖືກເລືອກ.

Filename Sanitization: ຟັງຊັນ sanitize_filename ເອົາຕົວອັກສອນທີ່ຜິດກົດໝາຍໃນຊື່ໄຟລ໌, ເຊັ່ນ: \/:*?"<>|. ນີ້ຮັບປະກັນວ່າຂໍ້ຄວາມທີ່ສະກັດອອກມາສາມາດຖືກນໍາໃຊ້ຢ່າງປອດໄພເປັນຊື່ໄຟລ໌.

ການຈໍາກັດຊື່ໄຟລ໌: ຊື່ໄຟລ໌ຜົນຜະລິດຖືກຈໍາກັດພຽງແຕ່ 50 ຕົວອັກສອນທໍາອິດຂອງວັກເພື່ອຫຼີກເວັ້ນການຊື່ໄຟລ໌ຍາວເກີນໄປ.

ການເລືອກສຽງ: ສະຄຣິບຍັງອະນຸຍາດໃຫ້ປ່ຽນລະຫວ່າງສຽງເພດຊາຍ ແລະສຽງຜູ້ຍິງໂດຍອີງໃສ່ການສະຫຼັບ use_male_voice.

ຜົນຜະລິດ:
ຊື່ໄຟລ໌ສຽງ: 50 ຕົວອັກສອນທໍາອິດຂອງວັກທໍາອິດຈາກໄຟລ໌ຂໍ້ຄວາມຈະຖືກໃຊ້ເປັນຊື່ໄຟລ໌ MP3 ຜົນຜະລິດ.
ນີ້ຄວນຈະຕອບສະຫນອງຄວາມຕ້ອງການຂອງທ່ານສໍາລັບການສະກັດວັກທໍາອິດແລະນໍາໃຊ້ມັນເປັນຊື່ໄຟລ໌ຜົນຜະລິດ.


ການປ່ານສຽງສາມາດເບິ່ງໄດ້ທີ່ https://github.com/hasscc/hass-edge-tts/blob/main/custom_components/edge_tts/tts.py

source: https://github.com/rany2/edge-tts