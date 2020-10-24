#ifndef DLLIST_H
#define DLLIST_H

struct dllist {
  char * str;
  struct dllist * next;
  struct dllist * prev;
};

struct dllist *
dllist_init(const char * str);

struct dllist *
dllist_find(struct dllist * dllist, const char * str);

struct dllist *
dllist_unlink(struct dllist * node);

void
dllist_append(struct dllist * dllist, const char * str);

void
dllist_insert_after(struct dllist * node, const char * str);

void
dllist_free(struct dllist * dllist);

#endif
