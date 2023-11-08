#include <Python.h>

/* Prototypes */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints basic info about python list
 * @p: pointer to python list
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;

	size = ((PyVarObject *)p)->ob_size;
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (!strcmp(item->ob_type->tp_name, "bytes"))
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - prints basic info about python bytes
 * @p: pointer to python bytes
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;

	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %ld bytes:", size);
	for (i = 0; i < size; i++)
		printf(" %02hhx", ((PyBytesObject *)p)->ob_sval[i]);
	printf("\n");
}

/************************************************************************/

PyObject *list_handler(PyObject __attribute__((unused))*self, PyObject *args)
{
	PyObject *list;

	list = NULL;
	PyArg_ParseTuple(args, "o", list);
	print_python_list(list);
	return (NULL);
}

PyObject *bytes_handler(PyObject __attribute__((unused))*self, PyObject *args)
{
	PyObject *bytes;

	bytes = NULL;
	PyArg_ParseTuple(args, "o", bytes);
	print_python_bytes(bytes);
	return (NULL);
}

static PyMethodDef methods[] = {
	{"print_python_list", list_handler, METH_VARARGS, "listInfo"},
	{"print_python_bytes", bytes_handler, METH_VARARGS, "bytesInfo"},
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

PyMODINIT_FUNC PyInit_libPyList(void)
{
	return (PyModule_Create(&libPyList));
}
