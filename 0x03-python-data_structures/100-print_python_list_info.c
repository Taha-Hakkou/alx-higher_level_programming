#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to a Python object
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;

	if (PyList_CheckExact(p)) /* what for an instance of a subtype of the list type ? */
	{
		size = PyList_Size(p); /* or Py_SIZE(o) which expands for ((PyVarObject*)o)->ob_size */
		alloc = ((PyListObject*)p)->allocated;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", alloc);
		for (i = 0; i < size; i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
			/* Py_Type(o) expands for ((PyObject*)o)->ob_type */
		}
	}
	else
	{
		printf("Not a list\n"); /* need a nice error handling */
	}
}

PyObject *handler(PyObject __attribute__((unused))*self, PyObject *args)
{
	PyObject *list;

	list = NULL;
	PyArg_ParseTuple(args, "o", list);
	print_python_list_info(list);
	return (NULL);
}

static PyMethodDef methods[] = {
	{"print_python_list_info", handler, METH_FASTCALL, "listInfo"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef libPyList = {
	PyModuleDef_HEAD_INIT,
	"libPyList",
	"__doc__",
	-1,
	methods,
	NULL,
	NULL,
	NULL,
	NULL
};

PyMODINIT_FUNC PyInit_libPyList()
{
	return PyModule_Create(&libPyList);
}
