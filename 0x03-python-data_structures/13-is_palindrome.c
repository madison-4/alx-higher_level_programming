#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head of the linked ;list
 * Return: 1 if it is, 0 if it is not
 */
int is_palindrome(listint_t **head)
{

	listint_t *fast, *slow, *iter = *head, *prev_slow;
	if (*head == NULL)
		return (1);
	fast = iter;
	slow = iter;
	while ((fast != NULL) && (fast->next != NULL))
	{
		fast = fast->next->next;
		prev_slow = slow;
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
		nextref = current->next;
		current-> next = prev;
		prev = current;
		current = nextref;
	}
	*head = prev;
	return (prev);
}
/**
 * comparelist - copare two lists and find if they're equal
 * @head1: head of first list
 * @head2: head of second list
 * Return: 1 if they are, 0 if they aren't
 */
int comparelist(listint_t **head1, listint_t **head2)
{
