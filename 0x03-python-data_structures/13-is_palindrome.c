#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node, *next, *prev;

	prev = NULL;
	for (node = *head; node; node = next)
	{
		next = node->next;
		node->next = prev;
		prev = node;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to first node of linked list
 * Return: 1 if it's a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *node1, *node2;
	int length, i;

	node1 = *head;
	/* count length of linked list */
	length = 0;
	for (; node1; length++)
		node1 = node1->next;
	if (length < 2)
		return (1);
	/* reverse second half of the linked list */
	node1 = *head;
	for (i = 0; i < length / 2 - 1; i++)
		node1 = node1->next;
	node2 = reverse_listint(&(node1->next));
	/* check if palindrome */
	node1 = *head;
	for (i = 0; i < length / 2; i++)
	{
		if (node1->n != node2->n)
			return (0);
		if (i < length / 2 - 1)
		{
			node1 = node1->next;
			node2 = node2->next;
		}
	}
	/* re-arrange the linked list */
	reverse_listint(&(node1->next));
	return (1);
}
