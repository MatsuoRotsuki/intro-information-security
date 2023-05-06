#include <stdio.h>
#include <string.h>
int main ()
{
	/*char ciphertext[] = "bsaspp kkuosp";
	char key[] = "rsidpy dkawoa";
	char message [100] = "";
	for (int i = 0; i < strlen(ciphertext) ; i++)
	    printf("%d ", ciphertext[i] - 'a');
	printf("\n");
	for (int i = 0; i < strlen(ciphertext) ; i++)
	    printf("%d ", key[i] - 'a');
	printf("\n");
	for (int i = 0; i < strlen(ciphertext) ; i++)
	{
		if (ciphertext[i] != ' ')
		{
			if (ciphertext[i] > key[i])
			{
				printf("%c", ciphertext[i] - key[i] + 'a');
			}
			else if (ciphertext[i] < key[i])
			    printf("%c", 26 + ciphertext[i] - key[i] + 'a');
			else printf("%c",'a');	
		}
		else printf(" ");
	}
	message[strlen(ciphertext)] = '\0';
	*/
	printf("%x",'n'^0x4d^'k');
}
