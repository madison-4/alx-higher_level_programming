#include "lists.h"
/**
 * insert_node - inserts a node to a sorted linked list
 * @head: head of the linked list
 * @number: number part of the node in the list
 * Return: address of new node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *iter, *end;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (!(*head))
	{
		*head = new;
		return (new);
	}
	iter = *head;
	while (iter != NULL)
	{
		if (((iter->n) <= number) && ((iter->next->n) >= number))
		{
			new->next = iter->next;
			iter->next = new;
			return (new);
		}
		end = iter;
		iter = iter->next;
	}
	if (((*head)->n) > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	if ((end->n) < number)
	{
		end->next = new;
		new->next = NULL;
		return (new);
	}
	return (new);
}
