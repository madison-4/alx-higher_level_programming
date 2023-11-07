#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head of the linked ;list
 * Return: 1 if it is, 0 if it is not
 */
int is_palindrome(listint_t **head)
{

	listint_t *fast, *slow, *iter = *head;
	if (*head == NULL)
		return (1);
	fast = iter;
	slow = iter;
	while ((fast != NULL) && (fast->next != NULL))
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
/**
 * _reverselist - reverse a linkedlist
 * @head: head of the list to reerse
 * Return: New head,
 */
listint_t *_reverselist(listint_t **head)
{
	listint_t *prev = NULL, *current, *nextref;

	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current-> next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (prev);
}
