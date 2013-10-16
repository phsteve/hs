//initialize M[0] = 0
@0
M=0
@PREVIOUS
M=0


//Check if screen is full, if it is, terminate
//(LOOP)
//@8192
//D=A
//@0
//D=D-M
//@END
//D;JEQ
(LOOP)
@0
D=M
@8192
D=D-A
@RESETM
D;JEQ
@CONTINUE
0;JMP
(RESETM)
@0
M=0

(CONTINUE)
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
		M=0 //reset M[0] = 0
		@ONCONTINUE
		0;JMP //continue

	(ONCONTINUE)
		@SCREEN
		D=A
		@0
		D=D+M //go to next screen memory address
		A=D
		M=-1 //color it black
		@0
		M=M+1 //increment M[0]
	@LOOP
	0;JMP

(KEYOFF)
	@PREVIOUS
	D=M //look at previous
	M=0 //set it to 0
	//something is wrong right here
	@OFFCONTINUE
	D;JEQ //if key used to be off (previous=0), jump to offcontinue
	@OFFRESETM 
	D;JGT //if key used to be on (prev = 1), reset M

	(OFFRESETM)
		@0
		M=0 //reset M
		@OFFCONTINUE
		0;JMP 

	(OFFCONTINUE)
		@SCREEN
		D=A //store SCREEN in D
		@0
		D=D+M // D= SCREEN + M[0]
		A=D 
		M=0 //M[SCREEN + M[0]] = 0
		@0
		M=M+1 //increment M[0]
	@LOOP
	0;JMP

//(END)
//@END
//0;JMP




