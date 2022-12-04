#include <unistd.h>
#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

int length_of_list(listint_t *head)
{
	int len;

	for (len = 0; head; len++)
		head = head->next;

	return (len);
}

/**
*
*
*
*
*/

int is_palindrome(listint_t **head)
{
	int i, len, half, *entire;
	listint_t *temp = *head;

	if (!head)
		return (1);

	len = length_of_list(temp);
	entire = malloc(sizeof(int) * len);
	if (!entire)
		return (1);
	temp = *head;

	for (i = 0; temp; i++)
	{
		entire[i] = temp->n;
		temp = temp->next;
	}
	half = i / 2;

	for (i = 0; i <= half; i++)
	{
		if (entire[i] != entire[len - (i + 1)])
			return (0);
		else
			continue;
	}
	return (1);
}
