#include "lists.h"

/**
 * check_cycle - checks if a singly_linked list contains a cycle
 * @list: the list to check
 * Return: 0 if no cycle found, otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !(list->next))
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
