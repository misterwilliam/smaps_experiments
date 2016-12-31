#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char **argv)
{
  pid_t pid = getpid();
  printf("pid: %i\n", (int)pid);
  printf("cat /proc/%i/smaps\n", (int)pid);
  fgetc(stdin);
  return 0;
}
