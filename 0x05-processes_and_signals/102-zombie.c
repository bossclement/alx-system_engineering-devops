#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * endless - creates an endless loop
 *
 * Return: always 0 (success)
 */
int endless(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main function
 *
 * Return: always 0 (success)
 */
int main()
{
	pid_t pid;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid < 0)
			perror("fork error");
		else if (pid == 0)
			exit(0);
		printf("Zombie process created, PID: %ld\n", (long) pid);
	}
	endless();
	return (0);
}
