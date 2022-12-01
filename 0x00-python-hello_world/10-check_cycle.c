#include "lists.h"

/**
* check_cycle - check if a linked list has a cycle
* @list: pointer to elements in the list
*
* Return: 1 is cycle is found, 0 if not
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
