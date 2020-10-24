#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dllist.h"


struct dllist *
_dllist_create(const char * str)
{
  struct dllist * node = malloc(sizeof(struct dllist));
  if (node == NULL) {
    fprintf(stderr, "Could not allocate memory for dllist node.\n");
    exit(EXIT_FAILURE);
  }
  if (str != NULL) {
    size_t len_string = strlen(str);
    node->str = malloc(len_string+1);
    if (node->str == NULL) {
      fprintf(stderr, "Could not allocate memory for dllist string.\n");
      exit(EXIT_FAILURE);
    }
    strncpy(node->str, str, len_string);
    node->str[len_string] = '\0';
  }
  return node;
}


struct dllist *
dllist_init(const char * str)
{
  struct dllist * head = _dllist_create(str);
  head->next = head;
  head->prev = head;
  return head;
}


void
dllist_append(struct dllist * head, const char * str)
{
  struct dllist * last_new = _dllist_create(str);
  struct dllist * last = head->prev;

  last_new->next = head;
  last_new->prev = last;

  last->next = last_new;
  head->prev = last_new;
}


void
dllist_insert_after(struct dllist * node, const char * str)
{
  struct dllist * new = _dllist_create(str);
  new->prev = node;
  new->next = node->next;
  new->next->prev = new;
  new->prev->next = new;
}


void
dllist_free(struct dllist * node_start)
{
  struct dllist * current = node_start;
  for(;;) {
    if (current->str != NULL) {
      free(current->str);
    }
    struct dllist * next = current->next;
    free(current);
    current = next;
    if (current == node_start) {
      break;
    }
  }
}


struct dllist *
dllist_find(struct dllist * head, const char * str)
{
  struct dllist * current = head;
  for (;;) {
    if (strcmp(current->str, str) == 0) {
      return current;
    }
    current = current->next;
    if (current == head) {
      break;
    }
  }
  return NULL;
}
