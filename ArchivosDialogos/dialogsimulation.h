#ifndef DIALOGSIMULATION_H
#define DIALOGSIMULATION_H

#include <QDialog>

namespace Ui {
class DialogSimulation;
}

class DialogSimulation : public QDialog
{
    Q_OBJECT

public:
    explicit DialogSimulation(QWidget *parent = nullptr);
    ~DialogSimulation();

private:
    Ui::DialogSimulation *ui;
};

#endif // DIALOGSIMULATION_H
