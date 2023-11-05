#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to first node of linked list
 * Return: 1 if it's a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *node1, *node2;
	int length, i, j;

	node1 = *head;
	if (!node1)
		return (1);
	for (length = 1; node1->next; length++)
		node1 = node1->next;
	for (i = 0; i < length / 2; i++)
	{
		node1 = *head;
		node2 = *head;
		for (j = 0; j < i; j++)
			node1 = node1->next;
		for (j = 0; j < length - i - 1; j++)
			node2 = node2->next;
		if (node1->n != node2->n)
			return (0);
	}
	return (1);
}
