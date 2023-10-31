#include "lists.h"
/**
 * check_cycle - find if a singly linked lists has a cycle
 * @list: head of the list
 * Return: 1 if it does, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *iter, *fast, *slow;

	iter = list;
	fast = iter;
	slow = iter;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
