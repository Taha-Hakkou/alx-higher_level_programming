#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of linked list
 * @number: number to insert
 * Return: pointer to new node, otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *node;

	current = *head;
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;

	if (current == NULL || current->n >= number)
	{
		node->next = current;
		*head = node;
		return (node);
	}

	while (current && current->next && current->next->n < number)
		current = current->next;

	node->next = current->next;
	current->next = node;

	return (node);
}
