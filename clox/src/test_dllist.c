#include <stdlib.h>
#include <stdio.h>

#include "dllist.h"

int
main(void)
{
  struct dllist * list = dllist_init("First");
  dllist_append(list, "Second");
  dllist_append(list, "Third");
  dllist_append(list, "Fourth");

  struct dllist * node_third = dllist_find(list, "Third");
  struct dllist * node_null = dllist_find(list, "Fifth");

  dllist_insert_after(node_third, "Third and a half");

  printf("%s\n", node_third->next->str);

  dllist_free(list);
}
