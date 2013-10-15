//initialize M[0] = 0
@0
M=0
@PREVIOUS
M=0


//check keyboard input (either 1/(KEYON) or 0/(KEYOFF))
(LOOP)
@KBD
D=M //look at KBD
@KEYOFF //if the key is off, jump to KEYOFF
D;JEQ
@KEYON
0;JMP //otherwise jump to KEYON
//if M[@PREVIOUS] = M[@KBD]
//	jump to 
//else, increment M[0] and continue either (KEYON) or (KEYOFF)

(KEYON)
	@PREVIOUS
	D=M //Look at PREVIOUS
	M=1 //set PREVIOUS to 1
	@ONCONTINUE
	D;JGT //If Previous used to be 1, continue darkening the screen
	@ONRESETM
	D;JEQ //Else, reset M[0] to 0 to start darkening the screen from 0

	(ONRESETM)
		@0
		M=0
		@ONCONTINUE
		0;JMP

	(ONCONTINUE)
		@SCREEN
		D=A
		@0
		D=D+M
		A=D
		M=-1
		@0
		M=M+1
	@LOOP
	0;JMP

(KEYOFF)
	@PREVIOUS
	D=M
	M=0
	@OFFCONTINUE
	D;JEQ
	@OFFRESETM
	D;JGT

	(OFFRESETM)
		@0
		M=0
		@OFFCONTINUE
		0;JMP

	(OFFCONTINUE)
		@SCREEN
		D=A
		@0
		D=D+M
		A=D
		M=0
		@0
		M=M+1
	@LOOP
	0;JMP

(END)
@END
0;JMP




