#ifndef CONTROLRASFOR_H
#define CONTROLRASFOR_H

#include <QDialog>

namespace Ui {
class controlrasfor;
}

class controlrasfor : public QDialog
{
    Q_OBJECT

public:
    explicit controlrasfor(QWidget *parent = nullptr);
    ~controlrasfor();

private:
    Ui::controlrasfor *ui;
};

#endif // CONTROLRASFOR_H
